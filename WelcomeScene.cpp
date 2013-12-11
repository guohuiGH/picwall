#include "cocos2d.h"
#include "WelcomeScene.h"
#include "PlaneGameScene.h"

USING_NS_CC;

const char WelcomeScene::m_sMenuItem[] = "menu.png";

SEL_MenuHandler WelcomeScene::callbackFuncions[] =
{
	(SEL_MenuHandler)(&WelcomeScene::newGameMenu),
	(SEL_MenuHandler)(&WelcomeScene::optionMenu),
	(SEL_MenuHandler)(&WelcomeScene::aboutMenu),
	(SEL_MenuHandler)(&WelcomeScene::playAgainMenu)
};

bool WelcomeScene::init()
{
	bool bRet = false;
	do 
	{
		CCArray *pArray = CCArray::createWithCapacity(4);
		pArray->retain();

		for (int i = 0; i < 3; i++)
		{
			CCSprite* spriteNormal = CCSprite::create(m_sMenuItem, CCRectMake(126 * i, 33 * 0, 126, 33));
			CCSprite* spriteSelected = CCSprite::create(m_sMenuItem, CCRectMake(126 * i, 33 * 1, 126, 33));
			CCSprite* spriteDisabled = CCSprite::create(m_sMenuItem, CCRectMake(126 * i, 33 * 2, 126, 33));
			CCMenuItemSprite *item = CCMenuItemSprite::create(
				spriteNormal, spriteSelected, spriteDisabled,
				this, callbackFuncions[i]
				);
			pArray->addObject(item);
		}

		CCMenu *menu = CCMenu::create(
			(CCMenuItem*)pArray->objectAtIndex(0),
			(CCMenuItem*)pArray->objectAtIndex(1),
			(CCMenuItem*)pArray->objectAtIndex(2),
			NULL);
		menu->alignItemsVertically();

		CCSize sizeOfVisible = CCDirector::sharedDirector()->getVisibleSize();
		menu->setPosition(ccp(sizeOfVisible.width / 2, sizeOfVisible.height / 2));

		this->addChild(menu, 1);

		CCSprite *backGround = CCSprite::create("loading.png");
		backGround->setPosition(ccp(sizeOfVisible.width / 2, sizeOfVisible.height / 2));

		this->addChild(backGround, 0);

		CCSprite *logo = CCSprite::create("logo.png");
		logo->setPosition(ccp(sizeOfVisible.width / 2, sizeOfVisible.height - logo->getContentSize().height / 2));

		this->addChild(logo, 1);

		bRet = true;
	} while (0);
	return bRet;
}

void WelcomeScene::newGameMenu(CCObject *sender)
{
	PlaneGameScene *newScene = PlaneGameScene::create();
	CCDirector::sharedDirector()->replaceScene( newScene );
	newScene->release();
}
void WelcomeScene::optionMenu(CCObject *sender){}
void WelcomeScene::aboutMenu(CCObject *sender){}
void WelcomeScene::playAgainMenu(CCObject *sender){}