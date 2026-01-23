from ultralytics.models import YOLO

if __name__ == '__main__':
    model = YOLO(r"CCTSDB2021.pt", task='detect')
    model.val(data="CCTSDB2021vedai.yaml", workers=0, batch=1, name="val", imgsz=512, device='0')  # train the model
# 这里用了cosine learing rate，默认的是linear


