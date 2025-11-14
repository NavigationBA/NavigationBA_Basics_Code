import sys
from config_test import PATH_BASE, PATH_SRC
sys.path.append(PATH_BASE)
sys.path.append(PATH_SRC)

from src.main import main

if __name__ == "__main__":
    main()