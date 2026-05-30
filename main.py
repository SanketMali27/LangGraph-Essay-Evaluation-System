from graph import graph

essay = """
# The Impact of Artificial Intelligence on Modern Society

Artificial Intelligence (AI) has become one of the most transformative technologies of the 21st century. From healthcare and education to transportation and business, AI is reshaping the way people live and work. While its rapid development offers numerous opportunities, it also raises important ethical, social, and economic challenges that society must address.

One of the most significant advantages of AI is its ability to improve efficiency and productivity. Businesses use AI-powered systems to automate repetitive tasks, analyze large amounts of data, and make informed decisions. For example, customer service chatbots can provide instant support, while predictive analytics helps companies understand consumer behavior and optimize their operations. As a result, organizations can save time, reduce costs, and improve overall performance.

AI has also revolutionized the healthcare industry. Machine learning algorithms can assist doctors in diagnosing diseases more accurately and at earlier stages. AI-powered tools can analyze medical images, detect abnormalities, and recommend treatment plans. Furthermore, wearable devices equipped with AI can monitor patients' health in real time, helping prevent serious medical conditions before they become critical.

In the field of education, AI offers personalized learning experiences. Intelligent tutoring systems can adapt to individual learning styles and provide customized feedback. This enables students to learn at their own pace and overcome specific challenges more effectively. Additionally, AI can help educators identify struggling students and develop targeted interventions to improve learning outcomes.

Despite these benefits, AI presents several challenges. One major concern is job displacement. As automation becomes more advanced, certain jobs may become obsolete, particularly those involving repetitive tasks. While AI can create new employment opportunities, workers must develop new skills to remain competitive in the changing job market. Governments and educational institutions play a crucial role in supporting workforce reskilling and adaptation.

Another important issue is privacy and data security. AI systems rely heavily on large datasets, many of which contain sensitive personal information. If this data is mishandled or accessed by unauthorized parties, individuals' privacy may be compromised. Therefore, organizations must implement strong security measures and comply with ethical guidelines to protect user data.

In conclusion, Artificial Intelligence has the potential to significantly improve various aspects of modern society. Its applications in healthcare, education, and business demonstrate its ability to enhance efficiency and innovation. However, society must also address concerns related to employment, privacy, and ethics. By balancing technological advancement with responsible governance, humanity can maximize the benefits of AI while minimizing its risks.

"""

result = graph.invoke(
    {
        "essay": essay
    }
)

print(result["final_report"])