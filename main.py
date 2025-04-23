import kagglehub
import os
import shutil

def main():
    print("Initializing Dataset!")
    if initialize_dataset():
        print("Dataset initialized successfully!")
    else:
        print("Dataset initialization failed.")

def initialize_dataset():
    try:
        titanic_path, sugar_path = download_datasets()
        project_dir = prepare_project_directory("./datasets")
        return move_datasets(titanic_path, sugar_path, project_dir)
    except Exception as e:
        print(f"Error during dataset initialization: {e}")
        return False

def download_datasets():
    titanic_path = kagglehub.dataset_download("yasserh/titanic-dataset")
    print("Path to Titanic dataset files:", titanic_path)
    sugar_path = kagglehub.dataset_download("ak0212/global-sugar-consumption-trends-19602023")
    print("Path to Sugar Consumption dataset files:", sugar_path)
    return titanic_path, sugar_path

def prepare_project_directory(directory):
    project_dir = os.path.abspath(directory)
    if not os.path.exists(project_dir):
        os.makedirs(project_dir)
        print("Project directory created:", project_dir)
    return project_dir

def move_datasets(titanic_path, sugar_path, project_dir):
    titanic_file = os.path.join(titanic_path, "Titanic-Dataset.csv")
    sugar_file = os.path.join(sugar_path, "sugar_consumption_dataset.csv")

    if not validate_files_exist([titanic_file, sugar_file]):
        return False

    try:
        shutil.move(titanic_file, project_dir)
        shutil.move(sugar_file, project_dir)
        print(f"Datasets moved to {project_dir} successfully!")
        return True
    except Exception as e:
        print(f"Error moving datasets: {e}")
        return False

def validate_files_exist(files):
    for file in files:
        if not os.path.exists(file):
            print(f"File {file} does not exist.")
            return False
    return True

if __name__ == "__main__":
    main()


