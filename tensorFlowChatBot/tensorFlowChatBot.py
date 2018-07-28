import tensorflow as tf
import data_utils
import seq2seq_model

#training the encoder(input) and decoder(response) data
def train():

    encoder_data, decoder_data = data_utils.prepare_custom_data(gConfig['working_directory'])
    train_set = read_data(encoder_data, decoder_data)
    
    
    
#Creating the model
#imbedding the input and attention
def seq2seq_func(encoder_inputs, decoder_inputs, do_decode):
    return tf.nn.seq2seq.embedding_attention_seq2seq(
        encoder_inputs, decoder_inputs, cell,
        number_of_encoder_symbols = source_vocab_size, 
        number_of_decoder_symbols = target_vocab_size,
        embedding_size = size, 
        output_projection= output_projection,
        feed_previous=do_decode
    
    )
