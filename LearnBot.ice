#ifndef LEARNBOTICE_H
#define LEARNBOTICE_H

module LearnBotModule
{
	sequence <byte> imagenT;

	interface LearnBot
	{
		string command(string c);
		imagenT getImageFromRobot(int w, int h);
		void shutdown();
	};
};
  
#endif
