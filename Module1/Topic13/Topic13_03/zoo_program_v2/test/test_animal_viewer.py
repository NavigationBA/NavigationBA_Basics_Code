import sys
from config_test import PATH_BASE, PATH_SRC
sys.path.append(PATH_BASE)
sys.path.append(PATH_SRC)

from src.animal_viewer import display_animal

if __name__ == "__main__":
    display_animal("1")
    display_animal("2")
    display_animal("3")
    display_animal("4")