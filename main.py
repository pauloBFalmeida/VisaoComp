import cv2
from train import processFiles, trainSVM
from detector import Detector

# pastas com as imagens positivas e negativas do dataset
pos_dir = "images/gadoP"
neg_dir = "images/gadoN"

# video de teste de validação do modelo
video_file = "images/gado.mp4"

# Extracao das features da imagens e salvamento no arquivo pickle
# treinamento do modelo
# Roda o classificador sobre o video
# Escreve os resultados no video .avi
if __name__ == "__main__":

    # Extract HOG features, color histogram features, and spatial features
    # from sample images, then save the data to a pickle file. Note that if an
    # output filepath isn't specified, a default timestamped filename will
    # be generated.
    feature_data_filename = "feature_data.pkl"
    processFiles(pos_dir, neg_dir, recurse=True, hog_features=True,
        hist_features=True, spatial_features=True, output_file=True,
        output_filename=feature_data_filename)

    # Treinar e salvar o modelo
    classifier_data_filename = "classifier_data.pkl"
    trainSVM(filepath=feature_data_filename, output_file=True,
        output_filename=classifier_data_filename)

    # Instancia o detector
    detector = Detector().loadClassifier(filepath=classifier_data_filename)

    # Abre o video de teste
    cap = cv2.VideoCapture(video_file)

    # Executar o detector e salvar o video resultante em um arquivo avi
    detector.detectVideo(video_capture=cap, write=True)
