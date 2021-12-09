#参考https://github.com/CoderCharm/MallAPI/
from apps import create_app
app = create_app()
import uvicorn
if __name__ == '__main__':
    uvicorn.run("run:app")
