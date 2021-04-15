# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bahn <bahn@student.42seoul.kr>             +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/04/05 15:29:22 by bahn              #+#    #+#              #
#    Updated: 2021/04/15 12:49:46 by bahn             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME		= libasm.a

AR		= ar rc

CC		= gcc
NASM		= nasm

RM		= rm -rf

CFLAG		= -Wall -Werror -Wextra
AFLAG		= -f macho64

INC_DIR		= includes/
SRC_DIR		= srcs/
OBJ_DIR		= ./

INC_FILES	= libasm.h
SRC_FILES	= ft_write.s \
		  ft_read.s \
		  ft_strlen.s \
		  ft_strcmp.s \
		  ft_strcpy.s \
		  ft_strdup.s

SRC_FILES_BONUS	= ft_atoi_base.s

INC		= $(addprefix $(INC_DIR), $(INC_FILES))
SRCS		= $(addprefix $(SRC_DIR), $(SRC_FILES))
SRCS_BONUS	= $(addprefix $(SRC_DIR), $(SRC_FILES_BONUS))
OBJS		= $(SRCS:.s=.o)
OBJS_BONUS	= $(SRCS_BONUS:.s=.o)

all		: $(NAME)

bonus		: $(OBJS_BONUS)
		$(AR) $(NAME) $(OBJS_BONUS)
		ranlib $(NAME)

$(NAME)		: $(OBJS)
		$(AR) $(NAME) $(OBJS)
		ranlib $(NAME)

.s.o		: $(SRCS)
		$(NASM) -I$(INC) $(AFLAG) $< -o $@
	
clean		: 
		$(RM) $(OBJS)

fclean		: clean
		$(RM) $(NAME)

re		: fclean all

.PHONY		: all, clean, fclean, re, bonus
		



	  
	 
