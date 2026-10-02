"""Loopback-only static preview with byte ranges for seekable HTML video."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]


class PreviewHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.byte_range = None
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def send_head(self):
        self.byte_range = None
        path = Path(self.translate_path(self.path))
        header = self.headers.get('Range')
        if not header or not path.is_file():
            return super().send_head()
        size = path.stat().st_size
        match = re.fullmatch(r'bytes=(\d*)-(\d*)', header.strip())
        if not match or not size:
            self.send_error(400, 'Invalid byte range')
            return None
        start, end = match.groups()
        if not start:
            if not end or int(end) == 0:
                self.send_error(400, 'Invalid byte range')
                return None
            start, end = max(0, size - int(end)), size - 1
        else:
            start = int(start)
            end = min(int(end), size - 1) if end else size - 1
        if start >= size or end < start:
            self.send_response(416)
            self.send_header('Content-Range', f'bytes */{size}')
            self.send_header('Content-Length', '0')
            self.end_headers()
            return None
        source = path.open('rb')
        source.seek(start)
        self.byte_range = start, end
        self.send_response(206)
        self.send_header('Content-Type', self.guess_type(str(path)))
        self.send_header('Content-Length', str(end - start + 1))
        self.send_header('Content-Range', f'bytes {start}-{end}/{size}')
        self.send_header('Last-Modified', self.date_time_string(path.stat().st_mtime))
        self.end_headers()
        return source

    def end_headers(self):
        self.send_header('Accept-Ranges', 'bytes')
        super().end_headers()

    def copyfile(self, source, output):
        if self.byte_range is None:
            shutil.copyfileobj(source, output)
            return
        start, end = self.byte_range
        remaining = end - start + 1
        while remaining:
            chunk = source.read(min(65536, remaining))
            if not chunk:
                break
            output.write(chunk)
            remaining -= len(chunk)


if __name__ == '__main__':
    server = ThreadingHTTPServer(('127.0.0.1', 4173), PreviewHandler)
    print('Local preview: http://127.0.0.1:4173/ (video byte ranges enabled)', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
