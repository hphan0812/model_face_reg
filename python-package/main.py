import cv2
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image

app = FaceAnalysis(providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
app.prepare(ctx_id=0, det_size=(640, 640))
img = ins_get_image('Minh')
faces = app.get(img)
count = 0
for i in range(len(faces)):
    face = faces[i]
    box = face.bbox.astype(int)
    cv2.imwrite(f"{count}.png",img[box[1]:box[3],box[0]:box[2]])
    count += 1
rimg = app.draw_on(img, faces)
cv2.imwrite(f"/disk/sdc/hanh/model_face_reg/python-package/out_face/face_1.png", rimg)