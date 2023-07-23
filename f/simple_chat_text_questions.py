import os
import openai
openai.api_key=""

content = """
Policy Owner : Ironman
Effective Date: Nov 2022   , Contact Information: ABC@acd.com
PolicyID: 123456
Policy Name: Global Gifts, Ent  
Geography: Global

‘ABC Corp’ supports the idea of gift exchange, received or offered by any employee within the company. The company strictly impede the idea of favor amongst the staff.

Purpose
The Employee Gift policy aims to maintain uniformity in exchanging, distributing, and receiving gifts from the employees, including gratuity and rewards. The company firmly believes that no employees must be gifted to benefit from them as it negatively influences other employees’ morale.

Scope
The scope of the policy expands towards every employee regardless of their designation and department. It applies to all the permanent, temporary, and contract-based employees.

Guidelines
‘ABC Corp’ follows strict guidelines for the matter of gifts and prohibits any favoritism and bribe in the company.

The company strictly prohibits any solicitation of gifts or favors from employees, organizations, and agencies from which he deals regularly.

The employees receiving and distributing gifts must ensure that it does not influence any conflicts of interest or change of preferences.

The employee/team must not receive any gifts, donations, or services from customers, competitors, or business dealers.

Exceptions
Though the company remains firm on its decisions, here are some exceptions to be taken care of.
Authorities and employees may accept edible/entertainment/accommodation gifts of (value), and they must be shared with the maximum/all employees.
Authorities and employees may receive items of (value) that can be displayed in the company—for example, Flowers.
Authorities and employees may accept handmade items from children.
Authorities and employees may accept donations from a charity.
Authorities and employees may accept gifts with prior approval of the CEO.
Authorities and employees may accept gifts in return for serving the community.
Authorities and employees may accept gifts received as a team.
Procedure
When received a gift prohibiting the company policy, one must graciously decline or return it and communicate to the person about this policy.
If the offerer of the gift is unknown, it must be immediately donated to a charity or use for community purposes under the advice of the higher authority.
Policy Violation
The violation of this policy under any circumstances will not be treated as an unknown mistake, and actions will be taken against the person, resulting in the individual’s immediate suspension.


"""

messages_parsed= [
    {"role": "system" ,
     "content": content},
    {"role":"user",
     "content":" Does Firm ABC Crop has any policy related to gifts ?"} ]
def get_completion_from_messages(
        messages,
        model="gpt-3.5-turbo",
        temperature=0,
        max_tokens=3000):

    response= openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens)

    return response.choices[0].message["content"]

print(get_completion_from_messages(messages_parsed))
