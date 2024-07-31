import os
import numpy as np
from numpy.linalg import norm 

SSIM_THRESHOLD = 0.4

def getFeature(file_name):
    feature = np.load(file_name)
    return feature

def computeSSIM(feature1, feature2):
    cos = np.squeeze(feature1).dot(feature2)
    return cos

class FaceDB:
    def __init__(self) -> None:
        self.face_db = []
        self.dataset_path = "/disk/sdc/hanh/model_face_reg/python-package/out_face"
        print(f'FaceDB: {self.dataset_path}')
        self.load_faces()

    def load_faces(self):
        for subdir, dirs, files in os.walk(self.dataset_path):
            for file in files:
                m_face_info = dict()
                m_face_info['name'] = file.split('.')[0]
                m_face_info['feature'] = getFeature(f'{self.dataset_path}/{file}')
                self.face_db.append(m_face_info)

    def add_face(self, name, feature_file):
        m_face_info = {'name': name, 'feature': getFeature(feature_file)}
        self.face_db.append(m_face_info)

    def get_face(self, name):
        for face in self.face_db:
            if face['name'] == name:
                return face
        return None
    
    def update_face(self, name, new_feature_file):
        for face in self.face_db:
            if face['name'] == name:
                face['feature'] = getFeature(new_feature_file)
                return True
        return False
    
    def delete_face(self, name):
        for i, face in enumerate(self.face_db):
            if face['name'] == name:
                del self.face_db[i]
                return True
        return False
    
    def search(self, feature_vector):
        current_cos = 0
        current_name = "unknown"
        for face_vec in self.face_db:
            m_cos = computeSSIM(feature_vector, face_vec['feature'])
            if m_cos > current_cos:
                current_name = face_vec['name']
                current_cos = m_cos
        if current_cos < SSIM_THRESHOLD:
            return "unknown", 0.0
        return current_name, current_cos
    
face_db = FaceDB()