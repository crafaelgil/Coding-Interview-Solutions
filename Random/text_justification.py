def justify_words(words, max_width):
  if not words or len(words) == 0:
    return []

words = ["this", "is", "an", "example", "of", "text", "justification."]
max_width = 16

print(justify_words(words, max_width))
