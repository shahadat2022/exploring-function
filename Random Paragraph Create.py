from random import choices

sentence_one =[
                'Starting a garden is just like real estate it\'s all about location.',
                'Place your garden in a part of your yard where you\'ll see it regularly (out of sight, out of mind '
                'definitely applies to gardening). ',
                'That way, you\'ll be much more likely to spend time in it.',
                'Misjudging sunlight is a common pitfall when you\'re first learning to garden.',
                'Pay attention to how sunlight plays through your yard before choosing a spot for your garden.',
                ]
sentence_two =[
                'Starting a garden is a lot like buying real estate in that location is everything.',
                'Your garden should be located in an area of your yard that you can easily view (out of sight,out of mind definitely applies to gardening).',
                'You\'ll be lot more inclined to spend time there if you do it that way.',
                'You will be far more likely to stay there if you do it that way.',
                'Prior to deciding where to place your garden, consider how the light interacts ',
                ]
sentence_three =[
                 'Just like buying real estate, location is crucial when starting a garden.',
                  'Put your garden in an area of your yard that you can easily access (out of sight, out of mind,definitely applies to gardening). ',
                  'You will be far more likely to stay there if you do it that way.',
                  'When you are initially learning to garden, it is typical to misjudge the amount of sunlight.',
                  'Before deciding where to place your garden, pay attention to how the sunshine flows through your yard.',
                  ]


def paragraph_formation(s1, s2, s3):
    """
This funchan will creat rendom paragraph
    :param s1,s2,s3: list of sentence
    :return: A paragraph
    """
    paragraph = choices(s1)+choices(s2)+choices(s3)
    return f'<p>{paragraph}</p>'
print(paragraph_formation(sentence_one, sentence_two, sentence_three))
print(paragraph_formation(sentence_one, sentence_two, sentence_three))
print(paragraph_formation(sentence_one, sentence_two, sentence_three))
print(paragraph_formation(sentence_one, sentence_two, sentence_three))
print(paragraph_formation(sentence_one, sentence_two, sentence_three))





