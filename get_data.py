"""Documentation for get_data.py


"""
import sys

#how do you get something in standard in?
#write tests with data already available

#stdin_data = input('type tab separated data here: ')
#print(stdin_data)


def read_stdin_col(col_num):
    """

    """
    # read in stdin
    data = sys.stdin.readline()
    # split on ';' into rows
    rows = data.split(';')
    # split on ' ' to divide columns
    split_columns = [y.split() for y in rows]
    # extract only the column of interest from each row
    desired_column = []
    for row in split_columns:
        desired_column.append(row[col_num])
    return desired_column


#def main():
#    A = read_stdin()
#    print(A[0])

#if __name__ == '__main__':
#    main()
