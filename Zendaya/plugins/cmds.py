#coding by @lallu_tg

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot.translation import Translation # pylint: disable=import-error

@Client.on_message(filters.command("start") & filters.private)
async def start(bot, update):
    
    buttons = [[
        InlineKeyboardButton('∂єν 1', url='https://t.me/Kallu_tg'),
        InlineKeyboardButton('∂єν 2', url ='https://t.me/TEAM_KERALA')
    ],[
        InlineKeyboardButton('ѕυρρσят', url='https://t.me/Edit_repo')
    ],[
        InlineKeyboardButton('нєℓρ', callback_data="help")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Spiderman.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )

@Client.on_message(filters.command("help") & filters.private)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Back🏃', callback_data='start'),
        InlineKeyboardButton('About🤔', callback_data='about')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )

@Client.on_message(filters.command("about") & filters.private)
async def about(bot, update):
    buttons = [[
        InlineKeyboardButton('Home🏃', callback_data='start'),
        InlineKeyboardButton('shut_down🔻', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html", 
        reply_to_message_id=update.message_id
    )
