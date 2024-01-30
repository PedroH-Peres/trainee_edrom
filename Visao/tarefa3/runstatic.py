from ultralytics import YOLO

model = YOLO('/home/arthur/Documents/Github/tarefa3edrom/runs/detect/train10/weights/best.pt')

results_img = model.predict(source='img2.jpg',  # image or video; single value or a list; URL, PIL (RGB), CV2 (BGR), ...
                        conf=0.25,
                        iou=0.7,  # Non-Maximum Supression (NMS)
                        imgsz=640,
                        show=True,
                        save=True,
                        save_txt=True,  # Save bbox coordenation
                        save_conf=True,  # save_txt must be True
                        save_crop=True,
                        # project='runs/detect',
                        stream=False  # Do inference now (False) or after (True)
                        )