from ultralytics.models import YOLO

if __name__ == '__main__':
    model = YOLO(r"D:/lzw/code/trained_model/CCTSDB2021/best.pt", task='detect')
    model.val(data="CCTSDB2021vedai.yaml", workers=0, batch=1, name="val_CCTSDB2021", imgsz=512, device='0')  # train the model
# 这里用了cosine learing rate，默认的是linear

