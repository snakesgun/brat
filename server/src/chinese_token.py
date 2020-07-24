#!/usr/bin/env python
# -*- coding: utf-8 -*-`

"""jieba wrapper for brat.

"""

import jieba
# Boundaries are on the form: [start, end]


def token_offsets_gen(text):
    # Parse in Wakati format
    # tagger = mecab.Tagger('-O wakati')
    # parse = tagger.parse(text)

    # Wakati inserts spaces, but only after non-space tokens.
    # We find these iteratively and then allow additional spaces to be treated
    # as separate tokens.

    # XXX: MeCab rapes newlines by removing them, we need to align ourselves
    # last_end = 0
    # for tok in (m.group(1) for m in WAKATI_REGEX.finditer(parse)):
    #     start = text.find(tok, last_end)
    #     end = start + len(tok)
    #     yield [start, end]
    #     last_end = end
    result = jieba.tokenize(text)
    for tk in result:
        yield [tk[1], tk[2]]


if __name__ == '__main__':
    # Minor test: Is it a duck? Maybe?
    sentence = '我爱北京天安门'
    token_offsets = [t for t in token_offsets_gen(sentence)]
    segmented = [sentence[start:end + 1] for start, end in token_offsets]
    print('\t'.join((sentence, str(token_offsets), '|'.join(segmented))))
