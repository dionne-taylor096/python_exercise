{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "0c3cbe76",
   "metadata": {},
   "source": [
    "# Question 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "cffc9a49",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "float"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(99.9)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "03a64a19",
   "metadata": {},
   "outputs": [],
   "source": [
    "type(\"False\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "49c92ec3",
   "metadata": {},
   "outputs": [],
   "source": [
    "type(False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a4fabe55",
   "metadata": {},
   "outputs": [],
   "source": [
    "type('0')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "920dae81",
   "metadata": {},
   "outputs": [],
   "source": [
    "type(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "867aa51e",
   "metadata": {},
   "outputs": [],
   "source": [
    "type([{}])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6f76580c",
   "metadata": {},
   "outputs": [],
   "source": [
    "type({'a': []})"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "166d9478",
   "metadata": {},
   "source": [
    "# Question 2\n",
    "\n",
    "2. What data type would best represent the following?\n",
    "\n",
    "- A term or phrase typed into a search box. String\n",
    "- Whether or not a user is logged in. Boolean\n",
    "- A discount amount to apply to a user's shopping cart. Float/int\n",
    "- Whether or not a coupon code is valid. String\n",
    "- An email address typed into a registration form. String\n",
    "- The price of a product. int/float\n",
    "- The email addresses collected from a registration form. String\n",
    "- Information about applicants to Codeup's data science program. Dictionary/String"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5fd0b2ae",
   "metadata": {},
   "source": [
    "# Question 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "a1bb5a01",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "can only concatenate str (not \"int\") to str",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[63], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43m1\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m \u001b[49m\u001b[38;5;241;43m+\u001b[39;49m\u001b[43m \u001b[49m\u001b[38;5;241;43m2\u001b[39;49m\n",
      "\u001b[0;31mTypeError\u001b[0m: can only concatenate str (not \"int\") to str"
     ]
    }
   ],
   "source": [
    "'1' + 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e7b84699",
   "metadata": {},
   "outputs": [],
   "source": [
    "6 % 4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6411c07b",
   "metadata": {},
   "outputs": [],
   "source": [
    "type (6 % 4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "22f4642b",
   "metadata": {},
   "outputs": [],
   "source": [
    "type(type(6 % 4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9ea4a256",
   "metadata": {},
   "outputs": [],
   "source": [
    "'3 + 4 is ' + 3 + 4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7946e0f9",
   "metadata": {},
   "outputs": [],
   "source": [
    "0 < 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6058b524",
   "metadata": {},
   "outputs": [],
   "source": [
    "'False' == False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a3d45524",
   "metadata": {},
   "outputs": [],
   "source": [
    "True == 'True'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5334e271",
   "metadata": {},
   "outputs": [],
   "source": [
    "5 >= -5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b01fa5d9",
   "metadata": {},
   "outputs": [],
   "source": [
    "True or \"42\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "604389bd",
   "metadata": {},
   "outputs": [],
   "source": [
    "6 % 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f5d63b26",
   "metadata": {},
   "outputs": [],
   "source": [
    "5 < 4 and 1 == 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "50764247",
   "metadata": {},
   "outputs": [],
   "source": [
    "'codeup' == 'codeup' and 'codeup' == 'Codeup'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5b081130",
   "metadata": {},
   "outputs": [],
   "source": [
    "4 >= 0 and 1 !== '1'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cddace98",
   "metadata": {},
   "outputs": [],
   "source": [
    "6 % 3 == 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b7ea4309",
   "metadata": {},
   "outputs": [],
   "source": [
    "5 % 2 != 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6b1b04b0",
   "metadata": {},
   "outputs": [],
   "source": [
    "[1] + 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aca87157",
   "metadata": {},
   "outputs": [],
   "source": [
    "[1] + [2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6adc0a40",
   "metadata": {},
   "outputs": [],
   "source": [
    "[1] * 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "abdf48c0",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "can't multiply sequence by non-int of type 'list'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[64], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[43m[\u001b[49m\u001b[38;5;241;43m1\u001b[39;49m\u001b[43m]\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43m \u001b[49m\u001b[43m[\u001b[49m\u001b[38;5;241;43m2\u001b[39;49m\u001b[43m]\u001b[49m\n",
      "\u001b[0;31mTypeError\u001b[0m: can't multiply sequence by non-int of type 'list'"
     ]
    }
   ],
   "source": [
    "[1] * [2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4565f40a",
   "metadata": {},
   "outputs": [],
   "source": [
    "[] + [] == []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4110c881",
   "metadata": {},
   "outputs": [],
   "source": [
    "{} + {}"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2876c96c",
   "metadata": {},
   "source": [
    "# Questions 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7076f14d",
   "metadata": {},
   "outputs": [],
   "source": [
    "the_little_mermaid = 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "773819f7",
   "metadata": {},
   "outputs": [],
   "source": [
    "brother_bear = 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "751b239c",
   "metadata": {},
   "outputs": [],
   "source": [
    "hercules = 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6a46b435",
   "metadata": {},
   "outputs": [],
   "source": [
    "daily_rent_fee = float(3.00)\n",
    "daily_rent_fee"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2f330ba9",
   "metadata": {},
   "outputs": [],
   "source": [
    "rental_cost = daily_rent_fee * the_little_mermaid\n",
    "rental_cost"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f4a9e843",
   "metadata": {},
   "source": [
    "# Questions 6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "886e2b5d",
   "metadata": {},
   "outputs": [],
   "source": [
    "hourly_rate_google = float(400.00)\n",
    "hourly_rate_facebook = float(350.00)\n",
    "hourly_rate_amazon = float(380.00)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fa8bfc3a",
   "metadata": {},
   "outputs": [],
   "source": [
    "daily_rate_google = hourly_rate_google * 6\n",
    "daily_rate_google"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f98a9cc5",
   "metadata": {},
   "outputs": [],
   "source": [
    "daily_rate_amazon = hourly_rate_amazon * 4\n",
    "daily_rate_amazon"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "55f61eb1",
   "metadata": {},
   "outputs": [],
   "source": [
    "daily_rate_facebook = hourly_rate_facebook * 10\n",
    "daily_rate_facebook"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "891662bc",
   "metadata": {},
   "outputs": [],
   "source": [
    "weekly_payment_amount = daily_rate_facebook + daily_rate_google + daily_rate_amazon\n",
    "round(weekly_payment_amount)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1a049bc2",
   "metadata": {},
   "source": [
    "# Questions 7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e7301c87",
   "metadata": {},
   "outputs": [],
   "source": [
    "class_not_full = False\n",
    "class_full = True\n",
    "class_schedule_no_conflicts = True\n",
    "class_schedule_conflict = False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b13112e8",
   "metadata": {},
   "outputs": [],
   "source": [
    "enrolled_student = class_not_full and class_schedule_conflict\n",
    "enrolled_student"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "89f07485",
   "metadata": {},
   "source": [
    "# Questions 8"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ca6d58d7",
   "metadata": {},
   "outputs": [],
   "source": [
    "more_than_two_items = True\n",
    "less_than_two_items = False\n",
    "offer_not_expired = True\n",
    "offer_expired = False\n",
    "premium_member = True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c37042b3",
   "metadata": {},
   "outputs": [],
   "source": [
    "product_offer_applied = less_than_two_items and offer_not_expired or premium_member\n",
    "product_offer_applied"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f5778d2b",
   "metadata": {},
   "outputs": [],
   "source": [
    "username = 'codeup'\n",
    "password = 'notastrongpassword'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f81e49a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "len(password) > 5 and len(username) >= 20 == True\n",
    "password != username == True\n",
    "password_count = password.count(\" \") > 0 == False\n",
    "username_count = username.count(\" \") > 0 == False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "336ec392",
   "metadata": {},
   "outputs": [],
   "source": [
    "pass_user_check = len(password) > 5 and len(username) <= 20 and password != username \n",
    "pass_user_check"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9ccbd7b4",
   "metadata": {},
   "outputs": [],
   "source": [
    "pass_user_char_check = password_count or username_count\n",
    "pass_user_char_check"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2b3bf73a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
