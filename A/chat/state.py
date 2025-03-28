import reflex as rx
import asyncio
from typing import List
from . import ai



class ChatMessage(rx.Base):
    message:str
    is_bot: bool = False
    



class ChatState(rx.State):
    did_submit: bool = False
    messages:List[ChatMessage]=[]
    @rx.var
    def user_did_submit(self)->bool:
        return self.did_submit
    
    
    def append_message(self,message,is_bot:bool=False):
        
        self.messages = self.messages + [ChatMessage(message=message,is_bot=is_bot)]
    #     self.messages.append(
    #         ChatMessage(
    #            message=message,
    #            is_bot = is_bot
    #        )
    #    )
    
    
    
    def get_gpt_messages(self):
        gpt_messages = [
        
        ]
        for chat_message in self.messages:
            role ='user'
            if chat_message.is_bot:
                role ='system'
            gpt_messages.append({
                "role":role,
                "content":chat_message.message
            })
            
        return gpt_messages    
                
    async def handle_submit(self,form_data:dict):
        print('here is our form data',form_data)
        user_message = form_data.get('message')
        if user_message:
            self.did_submit = True
            
            self.append_message(user_message,is_bot = False)
            yield 
            
            gpt_messages = self.get_gpt_messages()
            if not gpt_messages:
                print("Error: get_messages is None!")
                return 
            print("GPT messages:",gpt_messages)
            
            bot_response = ai.get__llm_response(gpt_messages)
            print("AI Response:",bot_response)
            if bot_response:
                self.append_message(bot_response,is_bot = True)
            else:
                print("Error:bot_response id None!")
                    
            # await asyncio.sleep(2)
            self.did_submit = False
            # self.append_message("This is a bot response",is_bot = True)
            
            yield 