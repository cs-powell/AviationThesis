// Downloaded from https://developer.x-plane.com/code-sample/simdata/


/*
 * SimData.c
 * 
 * This example demonstrates how to interact with X-Plane by reading and writing
 * data.  This example creates menus items that change the nav-1 radio frequency.
 * 
 */

#include <stdio.h>
#include <string.h>
// #include "XPLM/XPLMDataAccess.h"
// #include "XPLM/XPLMMenus.h"
#include <stdint.h>   // ADD THIS
#include <iostream>  // ADD THIS
// #include "XPLM/XPLMDataAccess.h"
// #include "XPLM/XPLMUtilities.h"    // Contains XPLMAppendMenuItem
// #include "XPLM/XPLMMenus.h"
// #include "XPLM/XPLMPlugin.h"
#include <iostream>
#include <fstream>

#include "SDK/CHeaders/XPLM/XPLMCamera.h"
#include "SDK/CHeaders/XPLM/XPLMDataAccess.h"
#include "SDK/CHeaders/XPLM/XPLMDefs.h"
#include "SDK/CHeaders/XPLM/XPLMDisplay.h"
#include "SDK/CHeaders/XPLM/XPLMGraphics.h"
#include "SDK/CHeaders/XPLM/XPLMMenus.h"
#include "SDK/CHeaders/XPLM/XPLMNavigation.h"
#include "SDK/CHeaders/XPLM/XPLMPlanes.h"
#include "SDK/CHeaders/XPLM/XPLMPlugin.h"
#include "SDK/CHeaders/XPLM/XPLMProcessing.h"
// #include "SDK/CHeaders/XPLM/XPLMScenery.h"
#include "SDK/CHeaders/XPLM/XPLMUtilities.h"
#include "SDK/CHeaders/XPLM/XPLMUtilities.h"
#include "SDK/CHeaders/XPLM/XPLMUtilities.h"
/* We keep our data ref globally since only one is used for the whole plugin. */
static XPLMDataRef gDataRef = NULL;
static XPLMDataRef pitch = NULL;
static XPLMDataRef roll = NULL;
static XPLMDataRef heading = NULL;
static XPLMFlightLoopID loopID = NULL;
static std::ofstream myfile;


float write(float inElapsedSinceLastCall, float inElapsedTimeSinceLastFlightLoop, int inCounter, void *inRefcon){
		float array[3] = {XPLMGetDataf(pitch), XPLMGetDataf(roll), XPLMGetDataf(heading)};
		// std::ofstream myfile;
		myfile << inElapsedSinceLastCall << "," << array[0] <<"," << array[1] <<"," << array[2] << "\n";
		myfile.flush();
		// XPLMDebugString("Nav1 frequency changed.\n");
		return -1.0;
	}

static void	MyMenuHandlerCallback(void *               inMenuRef,    void *               inItemRef);    
PLUGIN_API int XPluginStart(
						char *		outName,
						char *		outSig,
						char *		outDesc){


		XPLMMenuID	myMenu;
		int			mySubMenuItem;

	/* Provide our plugin's profile to the plugin system. */
	strcpy(outName, "SimData");
	strcpy(outSig, "xplanesdk.examples.simdata");
	strcpy(outDesc, "A plugin that changes sim data.");

	/* First we put a new menu item into the plugin menu.
	 * This menu item will contain a submenu for us. */
	mySubMenuItem = XPLMAppendMenuItem(
						XPLMFindPluginsMenu(),	/* Put in plugins menu */
						"Sim Data",				/* Item Title */
						0,						/* Item Ref */
						1);						/* Force English */
	
	/* Now create a submenu attached to our menu item. */
	myMenu = XPLMCreateMenu(
						"Sim Data", 
						XPLMFindPluginsMenu(), 
						mySubMenuItem, 			/* Menu Item to attach to. */
						MyMenuHandlerCallback,	/* The handler */
						0);						/* Handler Ref */
						
	/* Append a few menu items to our submenu.  We will use the refcon to
	 * store the amount we want to change the radio by. */
    XPLMAppendMenuItem(
        myMenu,
        "Decrement Nav1",
        (void*)(intptr_t)-1000,
        1);

    XPLMAppendMenuItem(
        myMenu,
        "Increment Nav1",
        (void*)(intptr_t)+1000,
        1);

	XPLMAppendMenuItem(
	myMenu,
	"Send Datafile",
	(void*)(intptr_t)+1000,
	1);

	



	
	
	/* Look up our data ref.  You find the string name of the data ref
	 * in the master list of data refs, including in HTML form in the 
	 * plugin SDK.  In this case, we want the nav1 frequency. */
	gDataRef = XPLMFindDataRef("sim/cockpit/radios/nav1_freq_hz");

	pitch = XPLMFindDataRef("sim/flightmodel/position/theta"); // pitch
	roll = XPLMFindDataRef("sim/flightmodel/position/phi");   // roll
	heading = XPLMFindDataRef("sim/flightmodel/position/psi");   // heading
	myfile.open ("/Users/flyingtopher/Applications/X-Plane 11/Data.txt");
	myfile << "Information About the Experiment Subject\n";
	myfile << "Data About their Machine, version, aircraft, device, etc.\n";
	myfile << "Experimental Data Begins Below:\n";
	myfile << "<sep>\n";
	myfile << "Pitch,Roll,Heading\n";
	myfile.flush();

	/* Only return that we initialized correctly if we found the data ref. */
	return (gDataRef != NULL) ? 1 : 0;
}

PLUGIN_API void	XPluginStop(void)
{
	myfile.close();

}

PLUGIN_API void XPluginDisable(void)
{
}

PLUGIN_API int XPluginEnable(void)
{
	return 1;
}



PLUGIN_API void XPluginReceiveMessage(
					XPLMPluginID	inFromWho,
					int				inMessage,
					void *			inParam)
{
}

void MyMenuHandlerCallback(void *inMenuRef, void *inItemRef)
{
    if (gDataRef != NULL) {
        int delta = (int)(intptr_t)inItemRef;   // SAFE CONVERSION
        XPLMSetDatai(gDataRef, XPLMGetDatai(gDataRef) + delta);
		// std::cout << "Nav1 frequency changed by " << delta << " Hz." << std::endl;
		//  XPLMDebugString("Nav1 frequency changed.");
		// float array[3] = {XPLMGetDataf(pitch), XPLMGetDataf(roll), XPLMGetDataf(heading)};
		// // std::ofstream myfile;
		// myfile << array[0] <<"," << array[1] <<"," << array[2] << "\n";
		// myfile.flush();
		XPLMDebugString("Entered menu callback\n");
		XPLMCreateFlightLoop_t params = {0};
		params.structSize = sizeof(XPLMCreateFlightLoop_t);
		params.phase = xplm_FlightLoop_Phase_BeforeFlightModel;
		params.callbackFunc = write;
		params.refcon = nullptr;
		loopID = XPLMCreateFlightLoop(&params);
		XPLMScheduleFlightLoop(loopID, 1, 1);
    }
}