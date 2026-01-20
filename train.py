from ultralytics.models import YOLO

if __name__=='__main__':
    model = YOLO(r"SRyolov8.yaml", task='detect')
    model.load("yolov8s.pt")
    model.train(data="CCTSDB2021vedai.yaml", epochs=100, workers=4, batch=4, save_period=10, cos_lr=True, name="exp1", imgsz=512, device='0')  # train the model
    # 这里用了cosine learing rate，默认的是linear

