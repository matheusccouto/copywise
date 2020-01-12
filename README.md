# copywise
Wisely copy files.
Select extensions to include or exclude while copying files.

### Prerequisites

```
Python 3.6+
```

### Installing

Use the package manager pip to install copywise.
```bash
pip install copywise
```

## Usage

```python
import copywise

copywise.copy_ext(src='Old Folder', dst='New Folder', include=['pdf', 'txt'])
copywise.copy_ext(src='Previous', dst='Next', exclude='zip')
```

## Author

* **Matheus Couto** - [Linkedin](https://www.linkedin.com/in/matheusccouto/)

## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License.

## Acknowledgments

* Originally created to copy only mobi files to a kindle devide, keeping folder structure.
However, it can be useful while backing up data.