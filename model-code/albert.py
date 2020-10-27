from transformers import AlbertTokenizer, AlbertConfig, TFAlbertModel

albert_mini_config = AlbertConfig(
    vocab_size = 50,
    embedding_size = 50,
    hidden_size = 50,
    num_hidden_layers = 2,
    num_hidden_groups = 1,  # default
    num_attention_heads = 10,
    intermediate_size = 100,
    inner_group_num = 1,  # default
    hidden_act = 'gelu_new',  # default
    hidden_dropout_prob = 0.,  # default
    attention_probs_dropout_prob = 0.,  # default
    max_position_embeddings = 50,
    type_vocab_size = 2,  # default
    initializer_range = 0.2,  # default
    layer_norm_eps = 1e-12,  # default
    classifier_dropout_probs = 0.1,  # default
    pad_token_id=0,  # default
    bos_token_id=2,  # default
    eos_token_id=3,  # default
)