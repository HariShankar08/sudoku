from PIL import Image
import numpy as np
import pytesseract
import matplotlib.pyplot as plt

'''Get the cells from the sudoku puzzle
Identify them as numbers or blank
Convert it to a list
Solve'''


def get_board(img_path):
    pytesseract.pytesseract.tesseract_cmd = 'tesseract/4.1.1/bin/tesseract'

    # Get the dimensions
    img = Image.open(img_path).convert('L')
    width, height = img.size
    cell_size = (round(width / 9), round(height / 9))
    img = np.array(img)

    img = [list(i) for i in img]
    img_iter = iter(img)

    rows = []
    try:
        col = 0
        sub = []
        while True:
            if col != cell_size[1]:
                sub.append(next(img_iter))
                col += 1
            else:
                rows.append(sub)
                sub = []
                col = 0
    except StopIteration:
        pass

    # print(np.array(rows)[0].shape)

    cells = []
    row_iter = iter(rows)
    try:
        start = 0
        while True:
            '''
            curr_row = next(row_iter)
            curr_row_cells = []
    
            while True:
                cell = [curr_row[i][start: start+cell_size[0]] for i in range(len(curr_row))]
                curr_row_cells.append(cell)
                start += cell_size[0]
                if start == width:
                    break
            '''
            curr_row = next(row_iter)
            curr_row_cells = []

            for i in range(width // cell_size[0]):
                cell = [curr_row[j][i * cell_size[0]: (i * cell_size[0]) + cell_size[0]] for j in range(len(curr_row))]
                curr_row_cells.append(cell)
            cells.append(curr_row_cells)

    except StopIteration:
        pass

    board = []
    for _ in range(9):
        board.append([0] * 9)

    for i in range(9):
        for j in range(9):
            cell = (np.array(cells)[i][j]).astype(np.uint8)
            plt.figure()
            plt.axis('off')
            plt.imshow(cell)
            plt.savefig('cell.png', bbox_inches='tight',
                        transparent=True,
                        pad_inches=0)
            plt.close()
            number = pytesseract.image_to_string('cell.png', config='--oem 3 --psm 6')
            if '1' in number:
                board[i][j] = 1
            else:
                for k in range(2, 10):
                    if str(k) in number:
                        board[i][j] = k

    return board


