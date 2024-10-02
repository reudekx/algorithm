from collections import defaultdict

def solution(genres, plays):
    song_dict = defaultdict(list)
    for num, genre in enumerate(genres):
        song_dict[genre].append((plays[num], num))
        
    sorted_dict = sorted(song_dict.items(), key=lambda x: sum(a for a, b in x[1]), reverse=True)
    
    answer = []

    for genre, songs in sorted_dict:
        songs.sort(key=lambda x: (-x[0], x[1]))
        answer.append(songs[0][1])
        if len(songs) > 1:
            answer.append(songs[1][1])

    return answer


'''
풀이 시간: 17분
접근:
    장르마다 총 개수를 세줘야 하고,
    장르별 노래마다 TOP 2를 골라야 한다.

후기:
    생각보다 정렬하는 게 까다로웠다.

'''