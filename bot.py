{\rtf1\ansi\ansicpg1252\cocoartf2907
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton\
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler, MessageHandler, filters\
import logging\
\
logging.basicConfig(\
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',\
    level=logging.INFO\
)\
\
PROGRAMS_DATA = \{\
    "summer": \{\
        "title": "\uc0\u1576 \u1585 \u1606 \u1575 \u1605 \u1580  \u1575 \u1604 \u1578 \u1583 \u1585 \u1610 \u1576  \u1575 \u1604 \u1589 \u1610 \u1601 \u1610 ",\
        "questions": \{\
            "q1": \{"text": "\uc0\u1605 \u1578 \u1609  \u1578 \u1606 \u1586 \u1604  \u1575 \u1604 \u1605 \u1603 \u1575 \u1601 \u1571 \u1577 \u1567 ", "answer": "\u1578 \u1606 \u1586 \u1604  \u1575 \u1604 \u1605 \u1603 \u1575 \u1601 \u1571 \u1577  \u1576 \u1593 \u1583  4 \u1571 \u1608  5 \u1571 \u1588 \u1607 \u1585  \u1605 \u1606  \u1575 \u1606 \u1578 \u1607 \u1575 \u1569  \u1575 \u1604 \u1576 \u1585 \u1606 \u1575 \u1605 \u1580 ."\},\
            "q2": \{"text": "\uc0\u1605 \u1578 \u1609  \u1575 \u1606 \u1578 \u1607 \u1609  \u1575 \u1604 \u1576 \u1585 \u1606 \u1575 \u1605 \u1580 \u1567 ", "answer": "\u1575 \u1606 \u1578 \u1607 \u1609  \u1575 \u1604 \u1576 \u1585 \u1606 \u1575 \u1605 \u1580  \u1601 \u1610  6 \u1571 \u1594 \u1587 \u1591 \u1587 ."\},\
            "q3": \{"text": "\uc0\u1605 \u1578 \u1609  \u1610 \u1576 \u1583 \u1571  \u1575 \u1604 \u1578 \u1587 \u1580 \u1610 \u1604 \u1567 ", "answer": "\u1604 \u1605  \u1610 \u1578 \u1605  \u1575 \u1604 \u1573 \u1593 \u1604 \u1575 \u1606  \u1593 \u1606  \u1575 \u1604 \u1605 \u1608 \u1593 \u1583  \u1576 \u1593 \u1583 ."\},\
            "q4": \{"text": "\uc0\u1605 \u1575  \u1605 \u1578 \u1591 \u1604 \u1576 \u1575 \u1578  \u1575 \u1604 \u1576 \u1585 \u1606 \u1575 \u1605 \u1580 \u1567 ", "answer": "1. \u1571 \u1606  \u1610 \u1603 \u1608 \u1606  \u1575 \u1604 \u1591 \u1575 \u1604 \u1576  \u1571 \u1608  \u1575 \u1604 \u1591 \u1575 \u1604 \u1576 \u1577  \u1576 \u1575 \u1604 \u1589 \u1601  \u1575 \u1604 \u1571 \u1608 \u1604  \u1571 \u1608  \u1575 \u1604 \u1579 \u1575 \u1606 \u1610  \u1571 \u1608  \u1575 \u1604 \u1579 \u1575 \u1604 \u1579 .\\n2. \u1571 \u1604 \u1575  \u1610 \u1603 \u1608 \u1606  \u1602 \u1583  \u1575 \u1604 \u1578 \u1581 \u1602  \u1576 \u1575 \u1604 \u1576 \u1585 \u1606 \u1575 \u1605 \u1580  \u1587 \u1575 \u1576 \u1602 \u1575 \u1611 .\\n3. \u1571 \u1604 \u1575  \u1610 \u1586 \u1610 \u1583  \u1593 \u1605 \u1585  \u1575 \u1604 \u1605 \u1578 \u1602 \u1583 \u1605  \u1593 \u1606  22 \u1587 \u1606 \u1577 ."\},\
            "q5": \{"text": "\uc0\u1605 \u1578 \u1609  \u1578 \u1589 \u1604  \u1575 \u1604 \u1588 \u1607 \u1575 \u1583 \u1577 \u1567 ", "answer": "\u1576 \u1593 \u1583  4 \u1571 \u1608  6 \u1571 \u1588 \u1607 \u1585  \u1605 \u1606  \u1575 \u1606 \u1578 \u1607 \u1575 \u1569  \u1575 \u1604 \u1576 \u1585 \u1606 \u1575 \u1605 \u1580 ."\}\
        \}\
    \},\
    "tamouh": \{\
        "title": "\uc0\u1576 \u1585 \u1606 \u1575 \u1605 \u1580  \u1591 \u1605 \u1608 \u1581 ",\
        "questions": \{\
            "q1": \{"text": "\uc0\u1605 \u1578 \u1609  \u1610 \u1615 \u1593 \u1602 \u1583  \u1608 \u1603 \u1605  \u1605 \u1583 \u1578 \u1607 \u1567 ", "answer": "\u1610 \u1576 \u1583 \u1571  \u1582 \u1604 \u1575 \u1604  \u1601 \u1589 \u1604  \u1575 \u1604 \u1589 \u1610 \u1601  \u1608 \u1610 \u1587 \u1578 \u1605 \u1585  \u1593 \u1604 \u1609  \u1605 \u1583 \u1575 \u1585  \u1575 \u1604 \u1593 \u1575 \u1605  \u1575 \u1604 \u1583 \u1585 \u1575 \u1587 \u1610  \u1604 \u1573 \u1603 \u1605 \u1575 \u1604  \u1605 \u1578 \u1591 \u1604 \u1576 \u1575 \u1578  \u1575 \u1604 \u1602 \u1576 \u1608 \u1604  \u1575 \u1604 \u1580 \u1575 \u1605 \u1593 \u1610 ."\},\
            "q2": \{"text": "\uc0\u1605 \u1575  \u1605 \u1578 \u1591 \u1604 \u1576 \u1575 \u1578  \u1575 \u1604 \u1576 \u1585 \u1606 \u1575 \u1605 \u1580 \u1567 ", "answer": "1. \u1571 \u1606  \u1578 \u1603 \u1608 \u1606  \u1591 \u1575 \u1604 \u1576 \u1575 \u1611 /\u1600 \u1577  \u1605 \u1587 \u1580 \u1604 \u1575 \u1611  \u1601 \u1610  \u1575 \u1604 \u1589 \u1601  \u1575 \u1604 \u1571 \u1608 \u1604  \u1571 \u1608  \u1575 \u1604 \u1579 \u1575 \u1606 \u1610  \u1575 \u1604 \u1579 \u1575 \u1606 \u1608 \u1610 .\\n2. \u1571 \u1604 \u1575  \u1610 \u1586 \u1610 \u1583  \u1593 \u1605 \u1585  \u1575 \u1604 \u1605 \u1578 \u1602 \u1583 \u1605  \u1593 \u1606  22 \u1587 \u1606 \u1577 .\\n3. \u1575 \u1604 \u1581 \u1589 \u1608 \u1604  \u1593 \u1604 \u1609  \u1573 \u1581 \u1583 \u1609  \u1588 \u1607 \u1575 \u1583 \u1575 \u1578  \u1575 \u1604 \u1604 \u1594 \u1577  \u1575 \u1604 \u1573 \u1606 \u1580 \u1604 \u1610 \u1586 \u1610 \u1577  \u1575 \u1604 \u1605 \u1593 \u1578 \u1605 \u1583 \u1577 ."\},\
            "q3": \{"text": "\uc0\u1605 \u1578 \u1609  \u1578 \u1589 \u1604  \u1575 \u1604 \u1588 \u1607 \u1575 \u1583 \u1577 \u1567 ", "answer": "\u1576 \u1593 \u1583  \u1571 \u1587 \u1576 \u1608 \u1593 \u1610 \u1606  \u1571 \u1608  \u1588 \u1607 \u1585  \u1593 \u1604 \u1609  \u1575 \u1604 \u1571 \u1602 \u1604  \u1605 \u1606  \u1575 \u1606 \u1578 \u1607 \u1575 \u1569  \u1575 \u1604 \u1576 \u1585 \u1606 \u1575 \u1605 \u1580 ."\}\
        \}\
    \},\
    "itc": \{\
        "title": "\uc0\u1576 \u1585 \u1606 \u1575 \u1605 \u1580  \u1575 \u1604 \u1603 \u1604 \u1610 \u1575 \u1578  \u1575 \u1604 \u1578 \u1602 \u1606 \u1610 \u1577  \u1608 \u1575 \u1604 \u1605 \u1607 \u1606 \u1610 \u1577  (ITC)",\
        "questions": \{\
            "q1": \{"text": "\uc0\u1605 \u1575  \u1575 \u1604 \u1605 \u1587 \u1575 \u1585 \u1575 \u1578  \u1575 \u1604 \u1578 \u1610  \u1610 \u1602 \u1576 \u1604 \u1607 \u1575  \u1575 \u1604 \u1576 \u1585 \u1606 \u1575 \u1605 \u1580 \u1567 ", "answer": "\u1610 \u1602 \u1576 \u1604  \u1580 \u1605 \u1610 \u1593  \u1575 \u1604 \u1605 \u1587 \u1575 \u1585 \u1575 \u1578 ."\},\
            "q2": \{"text": "\uc0\u1605 \u1575  \u1607 \u1610  \u1588 \u1585 \u1608 \u1591  \u1575 \u1604 \u1602 \u1576 \u1608 \u1604 \u1567 ", "answer": "1. \u1588 \u1607 \u1575 \u1583 \u1577  \u1575 \u1604 \u1579 \u1575 \u1606 \u1608 \u1610 \u1577 .\\n2. \u1606 \u1587 \u1576 \u1577  \u1575 \u1604 \u1579 \u1575 \u1606 \u1608 \u1610 \u1577  \u1575 \u1604 \u1593 \u1575 \u1605 \u1577  75% \u1601 \u1571 \u1593 \u1604 \u1609 .\\n3. \u1583 \u1585 \u1580 \u1577  \u1575 \u1582 \u1578 \u1576 \u1575 \u1585  \u1575 \u1604 \u1602 \u1583 \u1585 \u1575 \u1578  \u1575 \u1604 \u1593 \u1575 \u1605 \u1577  72% \u1601 \u1571 \u1593 \u1604 \u1609 .\\n4. \u1571 \u1604 \u1575  \u1610 \u1578 \u1580 \u1575 \u1608 \u1586  \u1593 \u1605 \u1585 \u1603  24 \u1587 \u1606 \u1577 .\\n5. \u1571 \u1604 \u1575  \u1610 \u1603 \u1608 \u1606  \u1602 \u1583  \u1605 \u1590 \u1609  \u1593 \u1604 \u1609  \u1578 \u1582 \u1585 \u1580 \u1603  \u1571 \u1603 \u1579 \u1585  \u1605 \u1606  3 \u1587 \u1606 \u1608 \u1575 \u1578 ."\}\
        \}\
    \},\
    "scholarship": \{\
        "title": "\uc0\u1576 \u1585 \u1575 \u1605 \u1580  \u1575 \u1604 \u1575 \u1576 \u1578 \u1593 \u1575 \u1579 ",\
        "questions": \{\
            "q1": \{"text": "\uc0\u1605 \u1575  \u1607 \u1610  \u1588 \u1585 \u1608 \u1591  \u1575 \u1604 \u1575 \u1576 \u1578 \u1593 \u1575 \u1579 \u1567 ", "answer": "1. \u1605 \u1606 \u1578 \u1592 \u1605  \u1601 \u1610  \u1575 \u1604 \u1589 \u1601  \u1575 \u1604 \u1579 \u1575 \u1604 \u1579  \u1575 \u1604 \u1579 \u1575 \u1606 \u1608 \u1610 .\\n2. \u1575 \u1604 \u1605 \u1593 \u1583 \u1604  \u1575 \u1604 \u1578 \u1585 \u1575 \u1603 \u1605 \u1610  \u1604 \u1575  \u1610 \u1602 \u1604  \u1593 \u1606  85%.\\n3. \u1605 \u1608 \u1575 \u1583  \u1593 \u1604 \u1605 \u1610 \u1577  \u1604 \u1575  \u1578 \u1602 \u1604  \u1593 \u1606  85%.\\n4. \u1575 \u1582 \u1578 \u1576 \u1575 \u1585  \u1575 \u1604 \u1602 \u1583 \u1585 \u1575 \u1578  \u1604 \u1575  \u1610 \u1602 \u1604  \u1593 \u1606  90%.\\n5. \u1575 \u1604 \u1593 \u1605 \u1585  \u1604 \u1575  \u1610 \u1586 \u1610 \u1583  \u1593 \u1606  22 \u1587 \u1606 \u1577 ."\}\
        \}\
    \}\
\}\
\
# \uc0\u1604 \u1608 \u1581 \u1577  \u1575 \u1604 \u1605 \u1601 \u1575 \u1578 \u1610 \u1581  \u1575 \u1604 \u1579 \u1575 \u1576 \u1578 \u1577  \u1578 \u1581 \u1578  \u1576 \u1575 \u1604 \u1571 \u1587 \u1601 \u1604 \
def get_persistent_keyboard():\
    keyboard = [\
        [KeyboardButton("\uc0\u55356 \u57312  \u1575 \u1604 \u1602 \u1575 \u1574 \u1605 \u1577  \u1575 \u1604 \u1585 \u1574 \u1610 \u1587 \u1610 \u1577  (/start)")]\
    ]\
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)\
\
def get_main_menu_inline():\
    return InlineKeyboardMarkup([\
        [InlineKeyboardButton(PROGRAMS_DATA["summer"]["title"], callback_data="prog_summer")],\
        [InlineKeyboardButton(PROGRAMS_DATA["tamouh"]["title"], callback_data="prog_tamouh")],\
        [InlineKeyboardButton(PROGRAMS_DATA["itc"]["title"], callback_data="prog_itc")],\
        [InlineKeyboardButton(PROGRAMS_DATA["scholarship"]["title"], callback_data="prog_scholarship")],\
        [InlineKeyboardButton("\uc0\u55356 \u57104  \u1605 \u1608 \u1602 \u1593  \u1575 \u1604 \u1576 \u1585 \u1575 \u1605 \u1580 ", url="https://armprograms.github.io/aramcoprograms/")],\
        [InlineKeyboardButton("\uc0\u1573 \u1585 \u1587 \u1575 \u1604  \u1575 \u1587 \u1578 \u1601 \u1587 \u1575 \u1585 ", callback_data="send_inquiry")]\
    ])\
\
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):\
    await update.message.reply_text(\
        "\uc0\u1571 \u1607 \u1604 \u1575 \u1611  \u1576 \u1603  \u1601 \u1610  \u1576 \u1585 \u1575 \u1605 \u1580  \u1571 \u1585 \u1575 \u1605 \u1603 \u1608 \u1548  \u1605 \u1575 \u1584 \u1575  \u1578 \u1608 \u1583  \u1575 \u1604 \u1575 \u1587 \u1578 \u1601 \u1587 \u1575 \u1585  \u1593 \u1606 \u1607 \u1567 ",\
        reply_markup=get_main_menu_inline()\
    )\
    await update.message.reply_text(\
        "\uc0\u1575 \u1587 \u1578 \u1582 \u1583 \u1605  \u1575 \u1604 \u1586 \u1585  \u1576 \u1575 \u1604 \u1571 \u1587 \u1601 \u1604  \u1604 \u1604 \u1593 \u1608 \u1583 \u1577  \u1604 \u1604 \u1602 \u1575 \u1574 \u1605 \u1577  \u1575 \u1604 \u1585 \u1574 \u1610 \u1587 \u1610 \u1577  \u1576 \u1571 \u1610  \u1608 \u1602 \u1578 :",\
        reply_markup=get_persistent_keyboard()\
    )\
\
async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):\
    text = update.message.text\
    if text == "\uc0\u55356 \u57312  \u1575 \u1604 \u1602 \u1575 \u1574 \u1605 \u1577  \u1575 \u1604 \u1585 \u1574 \u1610 \u1587 \u1610 \u1577  (/start)":\
        await update.message.reply_text(\
            "\uc0\u1571 \u1607 \u1604 \u1575 \u1611  \u1576 \u1603  \u1605 \u1606  \u1580 \u1583 \u1610 \u1583  \u1601 \u1610  \u1576 \u1585 \u1575 \u1605 \u1580  \u1571 \u1585 \u1575 \u1605 \u1603 \u1608 \u1548  \u1605 \u1575 \u1584 \u1575  \u1578 \u1608 \u1583  \u1575 \u1604 \u1575 \u1587 \u1578 \u1601 \u1587 \u1575 \u1585  \u1593 \u1606 \u1607 \u1567 ",\
            reply_markup=get_main_menu_inline()\
        )\
    else:\
        # \uc0\u1607 \u1606 \u1575  \u1610 \u1605 \u1603 \u1606 \u1603  \u1575 \u1587 \u1578 \u1602 \u1576 \u1575 \u1604  \u1571 \u1610  \u1606 \u1589  \u1578 \u1585 \u1587 \u1604 \u1607  \u1575 \u1604 \u1605 \u1587 \u1578 \u1582 \u1583 \u1605 \u1577  (\u1605 \u1579 \u1604  \u1575 \u1604 \u1575 \u1587 \u1578 \u1601 \u1587 \u1575 \u1585 \u1575 \u1578 ) \u1608 \u1575 \u1604 \u1578 \u1593 \u1575 \u1605 \u1604  \u1605 \u1593 \u1607 \
        await update.message.reply_text("\uc0\u1578 \u1605  \u1575 \u1587 \u1578 \u1604 \u1575 \u1605  \u1585 \u1587 \u1575 \u1604 \u1578 \u1603 \u1548  \u1587 \u1610 \u1578 \u1605  \u1605 \u1585 \u1575 \u1580 \u1593 \u1578 \u1607 \u1575  \u1608 \u1575 \u1604 \u1585 \u1583  \u1593 \u1604 \u1610 \u1603  \u1602 \u1585 \u1610 \u1576 \u1575 \u1611 .")\
\
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):\
    query = update.callback_query\
    await query.answer()\
    \
    data = query.data\
    \
    if data.startswith("prog_"):\
        prog_key = data.split("_")[1]\
        prog_info = PROGRAMS_DATA[prog_key]\
        \
        keyboard = []\
        for q_key, q_data in prog_info["questions"].items():\
            keyboard.append([InlineKeyboardButton(q_data["text"], callback_data=f"q_\{prog_key\}_\{q_key\}")])\
        keyboard.append([InlineKeyboardButton("\uc0\u55357 \u56601  \u1575 \u1604 \u1593 \u1608 \u1583 \u1577  \u1604 \u1604 \u1576 \u1585 \u1575 \u1605 \u1580 ", callback_data="back_main")])\
        \
        reply_markup = InlineKeyboardMarkup(keyboard)\
        await query.edit_message_text(text=f"\uc0\u1575 \u1604 \u1571 \u1587 \u1574 \u1604 \u1577  \u1575 \u1604 \u1588 \u1575 \u1574 \u1593 \u1577  \u1604 \u1600  \{prog_info['title']\}:", reply_markup=reply_markup)\
        \
    elif data.startswith("q_"):\
        _, prog_key, q_key = data.split("_")\
        answer_text = PROGRAMS_DATA[prog_key]["questions"][q_key]["answer"]\
        await context.bot.send_message(chat_id=update.effective_chat.id, text=answer_text)\
        \
    elif data == "send_inquiry":\
        await context.bot.send_message(\
            chat_id=update.effective_chat.id,\
            text="\uc0\u1578 \u1601 \u1590 \u1604  \u1576 \u1603 \u1578 \u1575 \u1576 \u1577  \u1575 \u1587 \u1578 \u1601 \u1587 \u1575 \u1585 \u1603  \u1607 \u1606 \u1575 \u1548  \u1608 \u1587 \u1610 \u1578 \u1605  \u1581 \u1601 \u1592 \u1607  \u1604 \u1604 \u1585 \u1583  \u1593 \u1604 \u1610 \u1607 ."\
        )\
        \
    elif data == "back_main":\
        await query.edit_message_text(\
            text="\uc0\u1571 \u1607 \u1604 \u1575 \u1611  \u1576 \u1603  \u1601 \u1610  \u1576 \u1585 \u1575 \u1605 \u1580  \u1571 \u1585 \u1575 \u1605 \u1603 \u1608 \u1548  \u1605 \u1575 \u1584 \u1575  \u1578 \u1608 \u1583  \u1575 \u1604 \u1575 \u1587 \u1578 \u1601 \u1587 \u1575 \u1585  \u1593 \u1606 \u1607 \u1567 ",\
            reply_markup=get_main_menu_inline()\
        )\
\
if __name__ == '__main__':\
    TOKEN = "8897871917:AAG4FIo9xpLKR0zmPddotjZ8rwevgi54dtE"\
    \
    app = ApplicationBuilder().token(TOKEN).read_timeout(30).write_timeout(30).build()\
    \
    app.add_handler(CommandHandler("start", start))\
    app.add_handler(CallbackQueryHandler(button_handler))\
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))\
    \
    app.run_polling()\
}