# Rememory Project

!\[Animation](.rememory.gif)

## Introduction

Rememory is a project focused on generating 3D visual designs. The project uses Python and leverages the power of the Pygame library to create intricate visual patterns and designs. Whether you're looking for rotating cubes, abstract patterns, or any form of digital art, Rememory has a module for it.

## Project Structure

```
rememory/
│
├── generation/                # Art generation modules.
│   ├── distorted_cube.py      # 3D rotating cube module.
│   ├── random_rectangles.py
│   ├── ...
│
├── processing/                # Infrastructure and display management.
│   ├── display.py             # Manages display/window setup.
│   ├── renderer.py            # Manages rendering and drawing frames.
│   ...
│
└── utils/
    ├── math_utils.py          # Mathematical utilities and transformations.
    └── ...
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/rememory.git
```

2. Navigate to the project directory:
```bash
cd rememory
```

3. Set up a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

4. Install the required packages:
```bash
pip install -r requirements.txt  # Assuming you have a requirements file.
```

### Running the Project

From the root directory, run:
```bash
python main.py
```

## Features

- **Dynamic 3D Designs**: Experience vibrant and evolving 3D designs that captivate the viewer.
- **Modular Architecture**: Easily add new art modules in the `generation` directory to expand the visual possibilities.
- **Customizable**: Tweak parameters, combine modules, or add your own to create unique visuals.
