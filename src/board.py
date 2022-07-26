import chess

import table


def evaluate_board(board):
    return sum(piece_value(board.piece_at(square), square) if board.piece_at(square) is not None else 0 for square in
               chess.SQUARES)


def piece_value(piece, square):
    symbol = piece.symbol()
    is_white = not symbol.islower()

    row = convert_square(square, is_white)[0]
    column = convert_square(square, is_white)[1]

    score = 1 if is_white else -1
    if symbol in ['pawn_black', 'pawn_white']:
        score *= (1000 + table.PAWN[row][column])
    elif symbol in ['knight_black', 'knight_white']:
        score *= (3000 + table.KNIGHT[row][column])
    elif symbol in ['bishop_black', 'bishop_white']:
        score *= (3000 + table.BISHOP[row][column])
    elif symbol in ['rook_black', 'rook_white']:
        score *= (5000 + table.ROOK[row][column])
    elif symbol in ['queen_black', 'queen_white']:
        score *= (9000 + table.QUEEN[row][column])
    elif symbol in ['king_black', 'king_white']:
        score *= (1000000 + table.KING[row][column])
    return score


def convert_square(square, is_white):
    row = 7 - (square // 8) if is_white else square // 8
    column = square % 8
    return row, column
