import tensorflow as tf
import data_utils
import seq2seq_model


def train():

    encoder_data, decoder_data = data_utils.prepare_custom_data()
   
