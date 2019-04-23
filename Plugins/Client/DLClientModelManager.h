// Copyright (c) 2019 The Foundry Visionmongers Ltd.  All Rights Reserved.
// This is strictly non-commercial.

#ifndef DLClientModelManager_H
#define DLClientModelManager_H

#include <string>
#include <vector>
#include "message.pb.h"

//! Class to parse and store knobs for a given model.
class DLClientModelManager
{
  public:
    explicit DLClientModelManager();
    ~DLClientModelManager();

    // Getters of the class
    int getNumOfFloats() const;
    int getNumOfInts() const;
    int getNumOfBools() const;
    int getNumOfStrings() const;
    int getNumOfButtons() const;

    std::string getDynamicBoolName(int idx);
    std::string getDynamicFloatName(int idx);
    std::string getDynamicIntName(int idx);
    std::string getDynamicStringName(int idx);
    std::string getDynamicButtonName(int idx);

    float* getDynamicFloatValue(int idx);
    int* getDynamicIntValue(int idx);
    bool* getDynamicBoolValue(int idx);
    std::string* getDynamicStringValue(int idx);
    bool* getDynamicButtonValue(int idx);
    void setDynamicButtonValue(int idx, int value);

    void clear();
    //! Parse the model options from the DL server.
    void parseOptions(const dlserver::Model& m);
    //! Update any current options from any changes to the DL server.
    void updateOptions(dlserver::Model& m);

  private:
    std::vector<int> _dynamicBoolValues;
    std::vector<int> _dynamicIntValues;
    std::vector<float> _dynamicFloatValues;
    std::vector<std::string> _dynamicStringValues;
    std::vector<int> _dynamicButtonValues;
    std::vector<std::string> _dynamicBoolNames;
    std::vector<std::string> _dynamicIntNames;
    std::vector<std::string> _dynamicFloatNames;
    std::vector<std::string> _dynamicStringNames;
    std::vector<std::string> _dynamicButtonNames;
};

#endif