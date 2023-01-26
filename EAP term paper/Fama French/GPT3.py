#%%

import os
import openai

#%%

%env OPENAI_API_KEY=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

openai.api_key = os.getenv("OPENAI_API_KEY")

#%% Template






response=openai.Completion.create(
  model="text-davinci-003",
  prompt="  ",
  max_tokens=2000,
  temperature=0.7,
  n=1,
  presence_penalty=0,
  frequency_penalty=0
)

print(response.choices[0].text)

#%%

'''

'''


#%%










#%%

openai.Completion.create(
  model="text-davinci-003",
  prompt=" does being selfish increase one's vulnerability to mental disorders ",
  max_tokens=2000,
  temperature=0.7,
  n=1,
  presence_penalty=0,
  frequency_penalty=0,
)

'''
Being selfish can increase one's vulnerability to mental disorders by creating a sense of isolation, 
which can lead to depression, anxiety, and other forms of mental distress. 
Selfish behavior can also lead to poor self-image and low self-esteem, 
which can lead to an increased risk of developing mental health issues. 
Additionally, selfish behavior can lead to interpersonal conflict, 
which can be a major source of stress and can also lead to problems with mental health.
'''



#%%

ans=openai.Completion.create(
  model="text-davinci-003",
  prompt=" give me some articles about that ",
  max_tokens=2000,
  temperature=0.7,
  n=1,
  presence_penalty=0,
  frequency_penalty=0
)

print(ans)

'''

'''


#%%

response=openai.Completion.create(
  model="text-davinci-003",
  prompt=" how to extract the text from openai response in Python ",
  max_tokens=2000,
  temperature=0.7,
  n=1,
  presence_penalty=0,
  frequency_penalty=0
)

print(response.choices[0].text)

#%%


'''
      "text": "\n\nThe OpenAI library provides functions to extract the text from a response. 
      To extract the text from an OpenAI response, you can use the `response.text` method. 
      For example: \n\n```python\nimport openai\n\n# Create the OpenAI client\nopenai.api_key = 
      \"your_api_key\"\n\n# Create the response object\nresponse = openai.Completion(engine=\"davinci\", 
      prompt=\"Hello world\")\n\n# Extract the text from the response\ntext = response.text\n\n# 
      Print the text\nprint(text)\n```"

'''


#%%


openai.Moderation.create(
  input="transgender and mental disorder",
)
















#%%



response=openai.Completion.create(
  model="text-davinci-003",
  prompt=" how is selfishness related to mental disorders ",
  max_tokens=2000,
  temperature=0.7,
  n=1,
  presence_penalty=0,
  frequency_penalty=0
)

print(response.choices[0].text)

#%%

'''
Selfishness can be related to certain mental disorders, such as narcissistic personality disorder. 
People with this disorder often have an excessive sense of entitlement, a need for admiration, and a lack of empathy for other people. 
They may also be overly self-centered and have difficulty considering the needs of others. 
Additionally, they may be more likely to engage in manipulative or exploitative behavior in order to get what they want.
'''


#%%

Q=" evidences and research articles about selfishness leading to mental disorder "

response=openai.Completion.create(
  model="text-davinci-003",
  prompt=Q,
  max_tokens=2000,
  temperature=0,
  n=1,
  presence_penalty=0,
  frequency_penalty=0
)
print(response.choices[0].text)


#%%

'''
1. "The Link Between Selfishness and Mental Illness" by Dr. Chris Gilbert.
2. "The Mental Health Consequences of Excessive Selfishness" by Robert L. Leahy.
3. "Selfishness and Its Impact on Mental Health" by Dr. Laura Markham.
4. "The Psychological Impact of Selfishness on Mental Health" by Scott E. Gilman.
5. "The Correlation between Selfishness and Mental Health" by Dr. John M. Grohol.
6. "The Role of Selfishness in Mental Disorders" by Dr. J. Mark Goulston.
7. "The Effects of Selfishness on Mental Health" by Dr. Jennifer Loh.
8. "The Relationship Between Selfishness and Mental Illness" by Dr. Mary Jo Rapini.
9. "The Impact of Selfishness on Mental Health" by Dr. Ellen Hendriksen.
10. "The Impact of Selfishness on Mental Health" by Dr. Amy Morin.
'''


#%%










Q=" altruism and depression "

response=openai.Completion.create(
  model="text-davinci-003",
  prompt=Q,
  max_tokens=2000,
  temperature=0,
  n=1,
  presence_penalty=0,
  frequency_penalty=0
)
print(response.choices[0].text)


#%%

'''
Altruism is the selfless concern for the well-being of others. 
It is often seen as a positive trait, as it can lead to increased social connections and improved mental health. 
Depression, on the other hand, is a mental health disorder characterized by persistent feelings of sadness, emptiness, and hopelessness.

Although altruism and depression are two distinct concepts, research has suggested that they may be linked in some way. 
Studies have found that people who engage in altruistic behaviors are less likely to experience depression. 
This could be due to the fact that altruism can lead to increased social connections and improved mental health, 
which can help to reduce the risk of depression. Additionally, altruism can provide a sense of purpose and meaning, 
which can help to reduce feelings of hopelessness and despair associated with depression.
'''


#%%










Q=" altruism and depression, citing from scientific research "

response=openai.Completion.create(
  model="text-davinci-003",
  prompt=Q,
  max_tokens=2000,
  temperature=0,
  n=1,
  presence_penalty=0,
  frequency_penalty=0
)
print(response.choices[0].text)


#%%

Q=" cite your previous respo "

response=openai.Completion.create(
  model="text-davinci-003",
  prompt=Q,
  max_tokens=2000,
  temperature=0,
  n=1,
  presence_penalty=0,
  frequency_penalty=0
)
print(response.choices[0].text)

#%%

Q="  summarize this article: Mental disorder and violence: personality dimensions and clinical features"

response=openai.Completion.create(
  model="text-davinci-003",
  prompt=Q,
  max_tokens=2000,
  temperature=0,
  n=1,
  presence_penalty=0,
  frequency_penalty=0
)
print(response.choices[0].text)

#%%

Q=" summarize this article in details: Psychosis and autism as diametrical disorders of the social brain "

response=openai.Completion.create(
  model="text-davinci-003",
  prompt=Q,
  max_tokens=2000,
  temperature=0,
  n=1,
  presence_penalty=0,
  frequency_penalty=0
)
print(response.choices[0].text)

#%%

Q="  "

response=openai.Completion.create(
  model="text-davinci-003",
  prompt=Q,
  max_tokens=2000,
  temperature=0,
  n=1,
  presence_penalty=0,
  frequency_penalty=0
)
print(response.choices[0].text)

#%%

Q="  "

response=openai.Completion.create(
  model="text-davinci-003",
  prompt=Q,
  max_tokens=2000,
  temperature=0,
  n=1,
  presence_penalty=0,
  frequency_penalty=0
)
print(response.choices[0].text)

#%%

Q="  "

response=openai.Completion.create(
  model="text-davinci-003",
  prompt=Q,
  max_tokens=2000,
  temperature=0,
  n=1,
  presence_penalty=0,
  frequency_penalty=0
)
print(response.choices[0].text)

#%%

Q="  "

response=openai.Completion.create(
  model="text-davinci-003",
  prompt=Q,
  max_tokens=2000,
  temperature=0,
  n=1,
  presence_penalty=0,
  frequency_penalty=0
)
print(response.choices[0].text)

#%%

Q="  "

response=openai.Completion.create(
  model="text-davinci-003",
  prompt=Q,
  max_tokens=2000,
  temperature=0,
  n=1,
  presence_penalty=0,
  frequency_penalty=0
)
print(response.choices[0].text)

#%%

Q="  "

response=openai.Completion.create(
  model="text-davinci-003",
  prompt=Q,
  max_tokens=2000,
  temperature=0,
  n=1,
  presence_penalty=0,
  frequency_penalty=0
)
print(response.choices[0].text)

#%%

Q="  "

response=openai.Completion.create(
  model="text-davinci-003",
  prompt=Q,
  max_tokens=2000,
  temperature=0,
  n=1,
  presence_penalty=0,
  frequency_penalty=0
)
print(response.choices[0].text)

#%%

Q='what time is it'

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=Q,
  temperature=0.5,
  max_tokens=60,
  top_p=0.3,
  frequency_penalty=0.5,
  presence_penalty=0.0
)

print(response.choices[0].text)

#%%

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Create an outline for an essay about Nikola Tesla and his contributions to technology:",
  temperature=0.3,
  max_tokens=150,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(response.choices[0].text)

#%%


response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Create an outline for an essay about Mental disorders, expectations and consumption decisions:",
  temperature=0.3,
  max_tokens=150,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

#%%

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Create an 2 page research proposal based on the following text:Depressed expectations: Mental disorders, expectations and consumption decisions Subjective expectations are the ultimate drivers of saving and consumption choices at the level of an individual and, when aggregated to the level of the entire economy, of macroeconomic outcomes (Gennaioli & Shleifer, 2018). Macroeconomists have recently moved to understand how individuals form, update and act upon their subjective economic expectations (e.g., D’Acunto et al., 2019). This substudy analyses how individuals’ mental health shapes their consumption decisions and the extent to which they are willing to borrow to finance their consumption. We expect mental health to affect individuals’ expectations, and in response to these expectations, their decision-making. Pessimistic ruminations and worry are symptoms of major depressive disorder, and we hypothesise that those with depressive disorder will have lower expectations of their future economic standing and the economy as a whole and thus, may be less inclined to buy big-ticket items (e.g., housing or cars) or borrow to finance their consumption. To account for the effect of individuals’ mental health on their future economic standing, we use individuals’ forecast errors in lieu of their expectations. Here, we define forecast error as the difference between individuals’ expected income or employment and their subsequent outcomes as observed in the register data. We also hypothesise that depressed individuals may be more inclined to express saving intentions to reduce their future financial worries. Worry is also a central symptom of generalised anxiety disorder, leading us to hypothesise the same effect for this disorder. Murphy et al. (2001) found that depressed patients exhibit greater risk aversion. Additionally, Leykin et al. (2011) and Germeijs and Verschueren (2011), among others, found that depression and trait anxiety are associated with indecisiveness. We are particularly interested in expectations and decision-making before and after the onset of COVID-19. For example, Ettman et al. (2020) found that the prevalence of depressive symptoms in the US was more than three times higher during the COVID-19 pandemic than before. This substudy aims to assess whether mental health-related changes in expectations and consumption have had a secondary effect on the macroeconomy, apart from COVID-19’s direct effect.",
  max_tokens=3500,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)


#%%

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with \"Unknown\".\n\nQ: What is human life expectancy in the United States?\nA: Human life expectancy in the United States is 78 years.\n\nQ: Who was president of the United States in 1955?\nA: Dwight D. Eisenhower was president of the United States in 1955.\n\nQ: Which party did he belong to?\nA: He belonged to the Republican Party.\n\nQ: What is the square root of banana?\nA: Unknown\n\nQ: How does a telescope work?\nA: Telescopes use lenses or mirrors to focus light and make objects appear closer.\n\nQ: Where were the 1992 Olympics held?\nA: The 1992 Olympics were held in Barcelona, Spain.\n\nQ: How many squigs are in a bonk?\nA: Unknown\n\nQ: Where is the Valley of Kings?\nA:",
  temperature=0,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\n"]
)

print(response.choices[0].text)

#%%

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="how to link overleaf with vs code",
  temperature=0,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.0,
)

print(response.choices[0].text)

#%%

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="how do i use it",
  temperature=0,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.0,
)

print(response.choices[0].text)

#%%