#ifndef LEARNBOTICE_H
#define LEARNBOTICE_H

module LearnBotModule
{
	interface LearnBot
	{
		string command(string c);
		void shutdown();
	};
};
  
#endif
