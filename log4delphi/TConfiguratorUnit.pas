{
   Copyright 2005-2006 Log4Delphi Project

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
}
{*----------------------------------------------------------------------------
   Contains the configuration procedures used to configure the Log4Delphi
   package.
   @version 0.5
   @author <a href="mailto:tcmiller@users.sourceforge.net">Trevor Miller</a>
  ----------------------------------------------------------------------------}
unit TConfiguratorUnit;

{$mode delphi}
{$h+}

interface

uses
  SysUtils, Forms,
  TLogLogUnit, TlevelUnit, TLoggerUnit,
  TPropertyConfiguratorUnit,
  TIniConfiguratorUnit;

type
  LoggerConfigurator = class
  public
    class procedure doBasicConfiguration;
    class procedure doPropertiesConfiguration(const fileName: String);
    class procedure doIniConfiguration(const fileName, sectionName: String);

    class procedure FinalCleanup;
  end;

implementation

{*----------------------------------------------------------------------------
   Use this method to quickly configure the logging suite.
  ----------------------------------------------------------------------------}
class procedure LoggerConfigurator.doBasicConfiguration;
begin
  TlogLogUnit.Initialize(ExtractFileDir(Application.ExeName) + '\log4delphi.log');
  Logger.Initialize();
end;

{*----------------------------------------------------------------------------
   This method performs a basic configuration and then configures the
   package based on the properties specified in the properties file.
  ----------------------------------------------------------------------------}
class procedure LoggerConfigurator.doPropertiesConfiguration(const fileName: String);
begin
  Logger.Initialize();
  PropertyConfigurator.DoConfigure(fileName);
end;

{*----------------------------------------------------------------------------
   This method performs a basic configuration and then configures the
   package based on the properties specified in the ini file section.
  ----------------------------------------------------------------------------}
class procedure LoggerConfigurator.doIniConfiguration(const fileName, sectionName: String);
begin
  Logger.Initialize();
  IniConfigurator.DoConfigure(fileName, sectionName);
end;

class procedure LoggerConfigurator.FinalCleanup;
begin
  Logger.FreeInstances;
  PropertyConfigurator.FreeAppenders;
end;

end.
 
