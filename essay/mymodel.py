from keras.preprocessing.sequence import pad_sequences
from keras.layers import Embedding, LSTM, Dense, Dropout
from keras.preprocessing.text import Tokenizer
from keras.callbacks import EarlyStopping
from keras.models import Sequential
import keras.utils as ku
import numpy as np
import os
from keras.models import load_model

tokenizer = Tokenizer()

def dataset_preparation(data):

    # basic cleanup
    corpus = data.lower().split("\n")

    # tokenization
    tokenizer.fit_on_texts(corpus)
    total_words = len(tokenizer.word_index) + 1

    # create input sequences using a list of tokens
    input_sequences = []
    for line in corpus:
        token_list = tokenizer.texts_to_sequences([line])[0]
        for i in range(1, len(token_list)):
            n_gram_sequence = token_list[:i+1]
            input_sequences.append(n_gram_sequence)

    # pad sequences
    max_sequence_len = max([len(x) for x in input_sequences])
    input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre'))

    # create predictors and label
    predictors, label = input_sequences[:,:-1], input_sequences[:,-1]
    label = ku.to_categorical(label, num_classes=total_words)

    return predictors, label, max_sequence_len, total_words

def generate_text(seed_text, next_words, max_sequence_len):
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
        predicted_probs = model.predict(token_list, verbose=0)[0]

        # Get the index of the word with the highest probability
        predicted_index = np.argmax(predicted_probs)

        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted_index:
                output_word = word
                break
        seed_text += " " + output_word
    return seed_text

training_folder_path = 'essay/Good'
training_data = ""

for filename in os.listdir(training_folder_path):
    if filename.endswith(".txt"):
        with open(os.path.join(training_folder_path, filename), 'r') as file:
            text = file.read().lower()
            training_data += text + "\n"

# Prepare the dataset
predictors, label, max_sequence_len, total_words = dataset_preparation(training_data)
model = load_model('essay/EssayTestModel.h5')

check_essay_text = "I look into the forest, moss wet on my feet. There’s fog everywhere—I can barely see the glasses that sit on my nose. I feel a cool breeze rustle against my coat. I am cold and warm all at once. The sun shines through the fog, casting the shadow of a tree whose roots know no end. At the entrance to the forest, I stand frozen in time and space. I can’t see what’s ahead of me or behind me, only what is. And what is suddenly transforms into what could be. I see a fork in the pathway in front of me. The noise—the noise is so loud. Crickets and owls and tigers, oh my. My thoughts scream even louder. I can’t hear myself think through the sounds of the forest of my mind. Off in the distance, I see a figure. It’s a shadow figure. It’s my mother. She’s walking towards me. I take a step into the forest, fearlessly ready to confront any overwhelming obstacle that comes my way. When I was a child, I used to play in the forest behind my house. Until one day when I caught my mom sneaking a cigarette outside. She tried to hide it behind her back, but I could see the smoke trailing over her head like a snail. I didn’t know what to do, so I ran farther into the forest. I am used to being disappointed by her. I ran and ran and ran until I tripped over a tree branch that fell in the storm the week before. I laid on the cold, hard ground. The back of me was soaked. Would I turn into my mom? After that, I decided to turn back. The cold was encroaching. I got home and saw my mom in the kitchen. We agreed not to speak of what I saw. While taking a history test, I looked around at my classmates. The gray desk was cold against my skin. I started counting the people around me, noting those who I knew well and those I had never really talked to. I looked at all the expensive backpacks and shoes. After our test, I asked the person next to me how she thought she did. She said it was a difficult test, and I agreed. Every class period, we’d talk more and more. We became friends. We started hanging out with another friend from biology class. We were inseparable, like three peas in a pod. We’d study together and hang out together and dance. They were the best friends I ever had. We liked to play soccer after school and sing loudly to music in my room. But one day it all stopped. They both stopped talking to me. It was like I had been yanked out of the forest and thrown on to the forest floor. I became moss, the owls pecking at my spikey green tendrils. They found two other friends, and I sat alone at my desk in history again. It was like another test, but this time a history of my own. Things went on like this for years. Over and over again I got put back into the forest. My friends who I thought were my friends actually were just drama machines. Life is foggy when you don’t know what’s going on. And I live in a forest that’s always foggy. Try as I might to find myself, it’s easy to get lost in all the trails and hills. I’m climbing a mountain each and every day. But I keep going back into the forest, looking for answers."

# def rewrite_mymodel(essay_data):
#   rewritten_essay = generate_text(essay_data, 1000, max_sequence_len)
#   return rewritten_essay

# rewrite_mymodel(check_essay_text)
def rewrite_mymodel(essay_data):
    chunks = [essay_data[i:i+500] for i in range(0, len(essay_data), 500)]
    rewritten_chunks = [generate_text(chunk, 200, max_sequence_len) for chunk in chunks]
    rewritten_essay = ' '.join(rewritten_chunks)
    return rewritten_essay