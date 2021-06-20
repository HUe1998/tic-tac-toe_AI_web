from django.http import HttpResponse, JsonResponse
import json
import ai.tictactoe as ttt


def ai_move(request):
    # request.body is a json sending the current board state
    if request.method == 'POST':
        board = json.loads(request.body)['board']
        move = ttt.minimax(board)
        res_board = ttt.result(board, move)
        return JsonResponse({"board": res_board})
    else:
        return HttpResponse(
            "Use only 'POST' request with a valid JSON as body"
        )
