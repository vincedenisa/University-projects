#pragma once
#include "service.h"
#define _CRT_SECURE_NO_WARNINGS

typedef struct
{
	Service* service;
}Ui;

Ui* createUI(Service* s);
void destroyUi(Ui* ui);

void startUi(Ui* ui);