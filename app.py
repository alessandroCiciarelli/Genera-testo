
import streamlit as st

import re

from aitextgen import aitextgen
from deep_translator import GoogleTranslator






def ai_text(inp,lunghezza, temp):
	ai = aitextgen()
	generated_text = ai.generate_one(max_length = lunghezza, prompt = inp, no_repeat_ngram_size = 3 , temperature = temp) #repetition_penalty = 1.9)
  #print(type(generated_text))
	return generated_text

def ittoen(testo):
	return GoogleTranslator(source='auto', target='en').translate(testo)

def entoit(testo):
	return GoogleTranslator(source='auto', target='it').translate(testo)


def saluti():
	st.markdown('<bold> Se ti è stato di aiuto condividi il nostro sito per supportarci </bold>\
	   <ul> \
	  <li><a href="https://www.facebook.com/sharer.php?u=http%3A%2F%2Fintelligenzaartificialeitalia.net%2F" target="blank" rel="noopener noreferrer">Condividi su Facebook</a></li> \
	  <li><a href="https://twitter.com/intent/tweet?url=http%3A%2F%2Fintelligenzaartificialeitalia.net%2F&text=Blog%2C+Forum%2C+Progetti%2C+e+Servizi+Gratuiti+completamente+dedicati+all%27+Intelligenza+Artificiale." target="blank" rel="noopener noreferrer">Condividi su Twitter</a></li> \
	  <li><a href="https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.intelligenzaartificialeitalia.net%2F&title=IntelligenzaArtificialeItalia=Blog%2C+Forum%2C+Progetti%2C+e+Servizi+Gratuiti+completamente+dedicati+all%27+Intelligenza+Artificiale.&source=IntelligenzaArtificialeItalia" target="blank" rel="noopener noreferrer">Condividi su Linkedin</a></li>\
	</ul>', unsafe_allow_html=True)





st.set_page_config(page_title="Genera Testi", page_icon="📚", layout='wide', initial_sidebar_state='auto')

st.markdown("<center><h1> Genera Testi, Articoli o Slogan con la nostra I.A. <small><br> Powered by INTELLIGENZAARTIFICIALEITALIA.NET </small></h1>", unsafe_allow_html=True)
st.write('<p style="text-align: center;font-size:15px;" > <bold>Stanco di doverti screvellare per scrivere un articolo o una presentazione ? <bold>  </bold> Da oggi ti ispiriamo noi<p><br>', unsafe_allow_html=True)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.subheader("GeneraTesti, Articoli o Slogan con la nostra rete Neurale !")



def main():

	inp = st.text_area('Scrivi una frase o un paragrafo di ispirazione per la nostra I.A.')

	col1, col2 = st.columns(2)		
	with col1:
		lunghezza = st.slider('Lunghezza massima del testo generato :', 50, 500,200,10)
	with col2:
		follia = st.slider('Controlla la "follia" del testo  :', 0.1, 1.1,0.7,0.1)

	
	if st.button("Genera testo") :
		nuovo = ittoen(inp)
		with st.spinner('Aspetta mentre la rete si allena...'):
			inp = ai_text(nuovo,lunghezza,follia)
		st.text_area('Testo generato', entoit(inp), height=400)

		saluti()
	
	st.text("")
	st.text("")
	st.text("")
	st.text("")
	st.text("")
	st.text("")
	st.text("")
	st.write("Proprietà intellettuale di [Intelligenza Artificiale Italia © ](https://intelligenzaartificialeitalia.net)")
	st.write("Hai un idea e vuoi realizzare un Applicazione Web Intelligente? contatta il nostro [Team di sviluppatori © ](mailto:python.ai.solution@gmail.com)")

if __name__ == '__main__':
	main()
