import shelve


def save_scores(score):
    shelf = shelve.open("scores.db")
    scores = shelf.get("scores", [])
    scores.append(score)
    shelf["scores"] = scores
    shelf.close()


def load_scores():
    shelf = shelve.open("scores.db")
    scores = shelf.get("scores", [])
    shelf.close()

    return sorted(scores, reverse=True)


if __name__ == "__main__":
    loaded_scores = load_scores()
    print(loaded_scores)
