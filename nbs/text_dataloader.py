from pathlib import Path

from fastai2.text.all import *
from fastai2.basics import *
from fastai2.callback.all import *


# Paths
corpus_path = Path('.bonltk/data/corpora/test-corpus')
tokenizer_models_path = Path('.bonltk/models/tokenizers')
lm_path = Path('.bonltk/models/lm')
lm_path.mkdir(exist_ok=True, parents=True)

seq_len = 72
seed = 43
valid_pct = 0.1


# Create Vocab
cls_ug_tok_fn = tokenizer_models_path/'classical-unigram.model'
cls_ug_tok = get_tokenizer(tok_func=SentencePieceTokenizer, lang='bo', sp_model=cls_ug_tok_fn)

vocab = [cls_ug_tok.tok.IdToPiece(int(i)) for i in range(30000)]
vocab[0] = 'xxunk'

dls = TextDataLoaders.from_folder(
    corpus_path,
    valid_pct=valid_pct, 
    seed=seed,
    text_vocab=vocab,
    is_lm=True,
    tok_tfm=Tokenizer(cls_ug_tok, rules=[]),
    seq_len=seq_len
)

dls.show_batch(max_n=3)
