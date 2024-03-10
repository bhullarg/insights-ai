from transformers import pipeline

def main():
    query = {
        'question': 'What are skills requried?',
        'context': 
        """
        STSI, the definitive nationwide technical placement firm, is at your service for the technical staffing needs of your company. As the business climate dictates the hiring of skilled individuals - STSI is there with quality staffing solutions who possess the precise skills, experience and educational requirements to fulfill your needs. STSI completes the void in your manpower with qualified individuals while allowing you to focus on the core undertaking of your business - prospering!
        """
    }
    
    ques_to_text = pipeline("question-answering", model="deepset/tinyroberta-squad2")
    answer = ques_to_text(query)['answer']
    print(answer)

main()