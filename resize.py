import os
import cv2

def process_images(input_dir, output_dir, categories, size=(100, 100)):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for category in categories:
        input_path = os.path.join(input_dir, category)
        output_path = os.path.join(output_dir, category)
        
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        
        for img_name in os.listdir(input_path):
            img_path = os.path.join(input_path, img_name)
            
            try:
                img = cv2.imread(img_path)
                if img is None:
                    print(f"Erro ao carregar: {img_path}")
                    continue
                
                img_resized = cv2.resize(img, size)
                cv2.imwrite(os.path.join(output_path, img_name), img_resized)
                print(f"Imagem processada: {img_name} -> {output_path}")
            except Exception as e:
                print(f"Erro ao processar {img_path}: {e}")

if __name__ == "__main__":
    dataset_dir = "dataset"
    output_base_dir = "processed_dataset"
    
    coletas = [f"ColetaAmostra{i}" for i in range(1, 6)]
    iron_fe = ["iron-Fe"]
    
    process_images(dataset_dir, os.path.join(output_base_dir, "ColetasAmostras"), coletas)
    process_images(dataset_dir, os.path.join(output_base_dir, "iron-Fe"), iron_fe)
    
    print("Processamento concluído!")

