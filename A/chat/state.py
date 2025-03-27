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
            {
                "role":"system",
                "message":"You are an expert at creating recipes like an elite chef.Respond in markdown"
            }
        ]
        for chat_message in self.messages:
            role ='user'
            if chat_message.is_bot:
                role ='system'
            gpt_messages.append({
                "role":role,
                "message":chat_message.message
            })
                
    async def handle_submit(self,form_data:dict):
        print('here is our form data',form_data)
        user_message = form_data.get('message')
        if user_message:
            self.did_submit = True
            
            self.append_message(user_message,is_bot = False)
            yield 
            gpt_messages = self.get_gpt_messages()
            bot_response = ai.get__llm_response(gpt_messages)
            # await asyncio.sleep(2)
            self.did_submit = False
            self.append_message("This is a bot response",is_bot = True)
            
            yield 