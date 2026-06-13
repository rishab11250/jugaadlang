[Setup]
AppName=JugaadLang
AppVersion={#MyAppVersion}
AppPublisher=JugaadLang Community
AppPublisherURL=https://jugaadlang.netlify.app
AppSupportURL=https://jugaadlang.netlify.app
AppUpdatesURL=https://jugaadlang.netlify.app
DefaultDirName={autopf}\JugaadLang
DefaultGroupName=JugaadLang
AllowNoIcons=yes
LicenseFile=..\LICENSE
OutputDir=..\dist
#ifndef MyArch
#define MyArch "amd64"
#endif
OutputBaseFilename=jugaadlang-setup-v{#MyAppVersion}-windows-{#MyArch}
SetupIconFile=compiler:SetupClassicIcon.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern
ChangesEnvironment=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "..\dist\jug.exe"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\JugaadLang REPL"; Filename: "{app}\jug.exe"; Parameters: "repl"
Name: "{group}\{cm:UninstallProgram,JugaadLang}"; Filename: "{uninstallexe}"

[Registry]
; Add to system PATH
Root: HKLM; Subkey: "SYSTEM\CurrentControlSet\Control\Session Manager\Environment"; \
    ValueType: expandsz; ValueName: "Path"; ValueData: "{olddata};{app}"; \
    Check: NeedsAddPath(ExpandConstant('{app}'))

[Code]
function NeedsAddPath(Param: string): boolean;
var
  OrigPath: string;
begin
  if not RegQueryStringValue(HKEY_LOCAL_MACHINE,
    'SYSTEM\CurrentControlSet\Control\Session Manager\Environment',
    'Path', OrigPath)
  then begin
    Result := True;
    exit;
  end;
  { look for the path with leading and trailing semicolon }
  { Pos() returns 0 if not found }
  Result := Pos(';' + Param + ';', ';' + OrigPath + ';') = 0;
end;
