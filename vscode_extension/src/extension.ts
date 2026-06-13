import * as vscode from 'vscode';
import * as path from 'path';

// ─────────────────────────────────────────────────────────────────────────────
// Keyword Map: JugaadLang → Python + description + funny Hindi phrase
// ─────────────────────────────────────────────────────────────────────────────
interface KeywordInfo {
  python: string;
  description: string;
  hindiQuote: string;
}

const KEYWORD_MAP: Record<string, KeywordInfo> = {
  bolo: {
    python: 'print',
    description: 'Print a value to the standard output.',
    hindiQuote: '💬 "Bol diya toh bol diya — ab sab sun lenge!"',
  },
  poochho: {
    python: 'input',
    description: 'Read a line of input from the user.',
    hindiQuote: '🤔 "Poochhhna koi buri baat nahi — data lo, kaam karo!"',
  },
  agar: {
    python: 'if',
    description: 'Conditional statement — executes block if condition is truthy.',
    hindiQuote: '🤷 "Agar sab theek hua toh seedha nahi toh... jugaad!"',
  },
  shayad: {
    python: 'elif',
    description: 'Else-if branch for additional conditions.',
    hindiQuote: '🎲 "Shayad yeh bhi kaam kare — try karte hain!"',
  },
  warna: {
    python: 'else',
    description: 'Else block — executes when all prior conditions are false.',
    hindiQuote: '😤 "Warna kya karein? Jugaad hi hai na!"',
  },
  ghumo: {
    python: 'for',
    description: 'For loop — iterate over a sequence.',
    hindiQuote: '🎡 "Ghumo ghumo — chakkar lagao aur kaam nikalo!"',
  },
  jabtak: {
    python: 'while',
    description: 'While loop — repeats as long as condition is true.',
    hindiQuote: '⏳ "Jabtak kaam nahi hua, tabtak rukna nahi!"',
  },
  banao: {
    python: 'def',
    description: 'Define a function.',
    hindiQuote: '🔧 "Banao ek function — phir baar baar use karo. Desi DRY!"',
  },
  wapas: {
    python: 'return',
    description: 'Return a value from a function.',
    hindiQuote: '🏠 "Kaam karke wapas aa gaye — value lekar!"',
  },
  ustad: {
    python: 'class',
    description: 'Define a class.',
    hindiQuote: '🎓 "Ustad kehte hain: class mein sab kuch seekho!"',
  },
  khud: {
    python: 'self',
    description: "Reference to the current instance of a class (Python's `self`).",
    hindiQuote: '🪞 "Khud ka khayal rakhna — self-referential wisdom!"',
  },
  lao: {
    python: 'import',
    description: 'Import a module or package.',
    hindiQuote: '📦 "Lao bhai lao — dusron ka kaam apne kaam aata hai!"',
  },
  se: {
    python: 'from',
    description: 'From — used with `lao` for selective imports.',
    hindiQuote: '🎯 "Se seedha — sirf jo chahiye woh lao, bakwaas nahi!"',
  },
  jaise: {
    python: 'as',
    description: 'Alias — define an alias name for an imported module or variable.',
    hindiQuote: '🎭 "Jaise ki matlab alias — chota naam, bada kaam!"',
  },
  as: {
    python: 'as',
    description: 'Alias — define an alias name for an imported module or variable.',
    hindiQuote: '🎭 "As/Jaise ki matlab alias — chota naam, bada kaam!"',
  },
  rukja: {
    python: 'break',
    description: 'Break out of a loop.',
    hindiQuote: '🛑 "Ruk ja yaar — itna ghoomna theek nahi!"',
  },
  chalte_raho: {
    python: 'continue',
    description: 'Skip the rest of the loop body and continue to next iteration.',
    hindiQuote: '🚶 "Chalte raho, chalte raho — bas ruk mat!"',
  },
  koshish: {
    python: 'try',
    description: 'Try block — attempt to execute potentially failing code.',
    hindiQuote: '💪 "Koshish karne walon ki kabhi haar nahi hoti!"',
  },
  gadbad: {
    python: 'except',
    description: 'Except block — handle exceptions.',
    hindiQuote: '🔥 "Gadbad ho gayi! Lekin hum sambhal lenge!"',
  },
  aakhir_me: {
    python: 'finally',
    description: 'Finally block — always executes, error or not.',
    hindiQuote: '🌅 "Aakhir mein, sab theek ho jaata hai — ya cleanup hota hai!"',
  },
  udao: {
    python: 'raise',
    description: 'Raise an exception.',
    hindiQuote: '🚀 "Udao exception — darr ko bhagao, problem ko highlight karo!"',
  },
  sahi: {
    python: 'True',
    description: 'Boolean True value.',
    hindiQuote: '✅ "Sahi matlab bilkul sahi — ekdum pakka!"',
  },
  galat: {
    python: 'False',
    description: 'Boolean False value.',
    hindiQuote: '❌ "Galat hua toh galat hua — maan lo aur aage badho!"',
  },
  kuch_nahi: {
    python: 'None',
    description: 'None — absence of a value.',
    hindiQuote: '🕳️ "Kuch nahi toh kuch nahi — shoonya ki bhi apni value hai!"',
  },
  aur: {
    python: 'and',
    description: 'Logical AND operator.',
    hindiQuote: '🤝 "Aur wala — dono sahi hone chahiye tabhi kaam banega!"',
  },
  ya: {
    python: 'or',
    description: 'Logical OR operator.',
    hindiQuote: '🔀 "Ya toh yeh, ya woh — ek kaam aaye toh kaafi!"',
  },
  nahi: {
    python: 'not',
    description: 'Logical NOT operator.',
    hindiQuote: '🙅 "Nahi matlab nahi — ekdum solid refusal!"',
  },
  tez: {
    python: 'async',
    description: 'Declare an asynchronous function.',
    hindiQuote: '⚡ "Tez chal — async programming mein intezaar nahi karte!"',
  },
  intezaar: {
    python: 'await',
    description: 'Await an asynchronous operation.',
    hindiQuote: '⏰ "Intezaar karo — async ka fal meetha hota hai!"',
  },
  baanto: {
    python: 'yield',
    description: 'Yield a value from a generator function.',
    hindiQuote: '🎁 "Baanto khushi — ek ek karke dena generator ki shaili hai!"',
  },
  theek_hai: {
    python: 'pass',
    description: 'Pass — do nothing (placeholder statement).',
    hindiQuote: '😴 "Theek hai yaar — kuch nahi karna, bas aage badho!"',
  },
  sabka: {
    python: 'global',
    description: 'Declare a global variable.',
    hindiQuote: '🌍 "Sabka — global variable, sab ka, sab ke liye!"',
  },
  chota_funkshan: {
    python: 'lambda',
    description: 'Lambda — anonymous function expression.',
    hindiQuote: '🐣 "Chota funkshan — nanha sa, ek line mein kaam karta hai!"',
  },
  mein: {
    python: 'in',
    description: 'Membership test operator or for-loop iteration.',
    hindiQuote: '🔍 "Mein hai ya nahi — yahi sab se bada sawaal!"',
  },
  bulawo: {
    python: '(function call)',
    description: 'Invoke or call a function.',
    hindiQuote: '📞 "Bulawo usse — function ko call karo, kaam karwa lo!"',
  },
  hai: {
    python: 'is',
    description: 'Identity operator — checks if two objects are the same.',
    hindiQuote: '🔎 "Hai ya nahi hai — yahi toh asli sawaal hai!"',
  },
  mein_nahi: {
    python: 'not in',
    description: 'Membership negation — checks if value is not in a sequence.',
    hindiQuote: '🚫 "Mein nahi — nahi mila, toh nahi mila!"',
  },
  nahi_hai: {
    python: 'is not',
    description: 'Identity negation — checks if two objects are NOT the same.',
    hindiQuote: '💔 "Nahi hai woh — alag alag hain yeh dono!"',
  },
  pakka: {
    python: 'assert',
    description: 'Assert — make sure a condition is true, otherwise raise an error.',
    hindiQuote: '🔒 "Pakka matlab pakka — isme koi shak nahi hona chahiye!"',
  },
  hatao: {
    python: 'del',
    description: 'Delete — remove a variable or item.',
    hindiQuote: '🗑️ "Hatao isse — memory se saaf karo!"',
  },
  gair_local: {
    python: 'nonlocal',
    description: 'Non-local scope declaration.',
    hindiQuote: '🏘️ "Gair local — na apna, na paraya, beech ka variable!"',
  },
  ke_saath: {
    python: 'with',
    description: 'With — context manager block for safe resource handling.',
    hindiQuote: '🤝 "Ke saath kaam karo — resources cleanly close ho jayenge!"',
  },
  chai: {
    python: 'chai() — JugaadLang stdlib',
    description: 'Print a motivational message with a virtual chai ☕.',
    hindiQuote: '☕ "Chai piyo, code karo — life simple hai!"',
  },
  himmat: {
    python: 'himmat() — JugaadLang stdlib',
    description: 'Raise courage — prints an encouraging desi quote.',
    hindiQuote: '💪 "Himmat rakho, jugaad lagao — sab theek ho jaayega!"',
  },
  jugaad: {
    python: 'jugaad() — JugaadLang stdlib',
    description: 'The ultimate jugaad — creative problem solving function.',
    hindiQuote: '🔧 "Jugaad hai toh solution hai — desi innovation zindabad!"',
  },
  kismat: {
    python: 'kismat(start, end) — JugaadLang stdlib',
    description: 'Returns a random number between start and end.',
    hindiQuote: '🎲 "Kismat pe bharosa mat kar, code likh!"',
  },
  sikka: {
    python: 'sikka() — JugaadLang stdlib',
    description: 'Flips a coin and returns Head or Tail.',
    hindiQuote: '🪙 "Sikka uchhalo, Head aaya toh ship, Tail aaya toh debug!"',
  },
  saaf: {
    python: 'saaf() — JugaadLang stdlib',
    description: 'Clears the terminal screen.',
    hindiQuote: '🧹 "Sab saaf kar do, naye sire se shuru karte hain!"',
  },
  ruk: {
    python: 'ruk(seconds) — JugaadLang stdlib',
    description: 'Pauses execution for the specified number of seconds.',
    hindiQuote: '⏸️ "Ruk ja bhai, processor ko thodi saans lene de!"',
  },
  bahar: {
    python: 'bahar() — JugaadLang stdlib',
    description: 'Exits the program immediately.',
    hindiQuote: '🚪 "Chalo bahar niklo, khel khatam!"',
  },
  namaste: {
    python: 'namaste() — JugaadLang stdlib',
    description: 'Displays a beautiful JugaadLang ASCII welcome banner.',
    hindiQuote: '🙏 "Namaste! Desi coding ki duniya mein swagat hai!"',
  },
  debug: {
    python: 'debug(variable) — JugaadLang stdlib',
    description: 'Prints out useful debugging information about a variable.',
    hindiQuote: '🐛 "Debug karna seekh lo, aadha dard wahin khatam!"',
  },
  version: {
    python: 'version() — JugaadLang stdlib',
    description: 'Displays the current installed version of JugaadLang.',
    hindiQuote: '🏷️ "Naya version, nayi umeed, naye bugs!"',
  },
  madad: {
    python: 'madad() — JugaadLang stdlib',
    description: 'Shows a massive custom Help Menu for JugaadLang functions.',
    hindiQuote: '📚 "Madad chahiye? Lo aagaya help menu!"',
  },
  pani_pilo: {
    python: 'pani_pilo() — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: pani_pilo',
    hindiQuote: '🎉 "pani_pilo ka maza lo!"',
  },
  soja: {
    python: 'soja() — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: soja',
    hindiQuote: '🎉 "soja ka maza lo!"',
  },
  crush: {
    python: 'crush() — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: crush',
    hindiQuote: '🎉 "crush ka maza lo!"',
  },
  proposal: {
    python: 'proposal(name) — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: proposal',
    hindiQuote: '🎉 "proposal ka maza lo!"',
  },
  couple_days: {
    python: 'couple_days() — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: couple_days',
    hindiQuote: '🎉 "couple_days ka maza lo!"',
  },
  breakup: {
    python: 'breakup() — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: breakup',
    hindiQuote: '🎉 "breakup ka maza lo!"',
  },
  love_percentage: {
    python: 'love_percentage(name1, name2) — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: love_percentage',
    hindiQuote: '🎉 "love_percentage ka maza lo!"',
  },
  attendance: {
    python: 'attendance() — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: attendance',
    hindiQuote: '🎉 "attendance ka maza lo!"',
  },
  assignment: {
    python: 'assignment() — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: assignment',
    hindiQuote: '🎉 "assignment ka maza lo!"',
  },
  exam_mode: {
    python: 'exam_mode() — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: exam_mode',
    hindiQuote: '🎉 "exam_mode ka maza lo!"',
  },
  cgpa: {
    python: 'cgpa() — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: cgpa',
    hindiQuote: '🎉 "cgpa ka maza lo!"',
  },
  bunk: {
    python: 'bunk() — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: bunk',
    hindiQuote: '🎉 "bunk ka maza lo!"',
  },
  motivation: {
    python: 'motivation() — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: motivation',
    hindiQuote: '🎉 "motivation ka maza lo!"',
  },
  stackoverflow: {
    python: 'stackoverflow() — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: stackoverflow',
    hindiQuote: '🎉 "stackoverflow ka maza lo!"',
  },
  deploy: {
    python: 'deploy() — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: deploy',
    hindiQuote: '🎉 "deploy ka maza lo!"',
  },
  git_push: {
    python: 'git_push() — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: git_push',
    hindiQuote: '🎉 "git_push ka maza lo!"',
  },
  ludo: {
    python: 'ludo() — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: ludo',
    hindiQuote: '🎉 "ludo ka maza lo!"',
  },
  snake_game: {
    python: 'snake_game() — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: snake_game',
    hindiQuote: '🎉 "snake_game ka maza lo!"',
  },
  tic_tac_toe: {
    python: 'tic_tac_toe() — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: tic_tac_toe',
    hindiQuote: '🎉 "tic_tac_toe ka maza lo!"',
  },
  rock_paper_scissors: {
    python: 'rock_paper_scissors() — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: rock_paper_scissors',
    hindiQuote: '🎉 "rock_paper_scissors ka maza lo!"',
  },
  guess_number: {
    python: 'guess_number() — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: guess_number',
    hindiQuote: '🎉 "guess_number ka maza lo!"',
  },
  hangman: {
    python: 'hangman() — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: hangman',
    hindiQuote: '🎉 "hangman ka maza lo!"',
  },
  meme: {
    python: 'meme() — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: meme',
    hindiQuote: '🎉 "meme ka maza lo!"',
  },
  joke: {
    python: 'joke() — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: joke',
    hindiQuote: '🎉 "joke ka maza lo!"',
  },
  roast: {
    python: 'roast() — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: roast',
    hindiQuote: '🎉 "roast ka maza lo!"',
  },
  pomodoro: {
    python: 'pomodoro(minutes) — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: pomodoro',
    hindiQuote: '🎉 "pomodoro ka maza lo!"',
  },
  todo: {
    python: 'todo() — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: todo',
    hindiQuote: '🎉 "todo ka maza lo!"',
  },
  habit_tracker: {
    python: 'habit_tracker() — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: habit_tracker',
    hindiQuote: '🎉 "habit_tracker ka maza lo!"',
  },
  focus_mode: {
    python: 'focus_mode() — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: focus_mode',
    hindiQuote: '🎉 "focus_mode ka maza lo!"',
  },
  study_with_me: {
    python: 'study_with_me() — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: study_with_me',
    hindiQuote: '🎉 "study_with_me ka maza lo!"',
  },
  ai_bhai: {
    python: 'ai_bhai(prompt) — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: ai_bhai',
    hindiQuote: '🎉 "ai_bhai ka maza lo!"',
  },
  resume_banao: {
    python: 'resume_banao() — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: resume_banao',
    hindiQuote: '🎉 "resume_banao ka maza lo!"',
  },
  interview_prep: {
    python: 'interview_prep() — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: interview_prep',
    hindiQuote: '🎉 "interview_prep ka maza lo!"',
  },
  roadmap: {
    python: 'roadmap(topic) — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: roadmap',
    hindiQuote: '🎉 "roadmap ka maza lo!"',
  },
  leetcode_bachao: {
    python: 'leetcode_bachao() — JugaadLang fun builtin',
    description: 'JugaadLang fun builtin: leetcode_bachao',
    hindiQuote: '🎉 "leetcode_bachao ka maza lo!"',
  },
};

// ─────────────────────────────────────────────────────────────────────────────
// Status Bar
// ─────────────────────────────────────────────────────────────────────────────
let statusBarItem: vscode.StatusBarItem;
let welcomeShown = false;

// ─────────────────────────────────────────────────────────────────────────────
// Activation
// ─────────────────────────────────────────────────────────────────────────────
export function activate(context: vscode.ExtensionContext): void {
  console.log('JugaadLang extension activated! 🇮🇳 Jai JugaadLang!');

  // ── Status Bar ──────────────────────────────────────────────────────────────
  statusBarItem = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Left, 100);
  statusBarItem.text = '🇮🇳 JugaadLang';
  statusBarItem.tooltip = 'JugaadLang — Desi coding ka raja!';
  statusBarItem.command = 'jugaadlang.runFile';
  context.subscriptions.push(statusBarItem);

  // Show/hide status bar based on active editor
  context.subscriptions.push(
    vscode.window.onDidChangeActiveTextEditor((editor) => {
      updateStatusBar(editor);
      if (editor && isJugFile(editor.document)) {
        maybeShowWelcome(context);
      }
    })
  );

  // Also check the currently active editor on startup
  updateStatusBar(vscode.window.activeTextEditor);

  // ── Hover Provider ──────────────────────────────────────────────────────────
  const hoverProvider = vscode.languages.registerHoverProvider(
    { language: 'jugaadlang', scheme: '*' },
    {
      provideHover(document, position) {
        const wordRange = document.getWordRangeAtPosition(position, /[a-zA-Z_][a-zA-Z0-9_]*/);
        if (!wordRange) {
          return undefined;
        }
        const word = document.getText(wordRange);
        const info = KEYWORD_MAP[word];
        if (!info) {
          return undefined;
        }

        const md = new vscode.MarkdownString('', true);
        md.isTrusted = true;
        md.supportHtml = true;

        md.appendMarkdown(`### 🇮🇳 \`${word}\` — JugaadLang Keyword\n\n`);
        md.appendMarkdown(`**Python equivalent:** \`${info.python}\`\n\n`);
        md.appendMarkdown(`${info.description}\n\n`);
        md.appendMarkdown(`---\n\n`);
        md.appendMarkdown(`*${info.hindiQuote}*\n`);

        return new vscode.Hover(md, wordRange);
      },
    }
  );
  context.subscriptions.push(hoverProvider);

  // ── Command: Run File ───────────────────────────────────────────────────────
  const runFileCmd = vscode.commands.registerCommand('jugaadlang.runFile', async () => {
    const editor = vscode.window.activeTextEditor;
    if (!editor) {
      vscode.window.showErrorMessage('JugaadLang: Koi file khuli nahi hai! Pehle file kholo.');
      return;
    }
    if (!isJugFile(editor.document)) {
      vscode.window.showErrorMessage('JugaadLang: Yeh .jug file nahi hai! Sahi file kholo.');
      return;
    }

    // Save before running
    if (editor.document.isDirty) {
      await editor.document.save();
    }

    const filePath = editor.document.uri.fsPath;
    const config = vscode.workspace.getConfiguration('jugaadlang');
    const jugPath = config.get<string>('jugPath', 'jug');
    const fileName = path.basename(filePath);

    const terminal = vscode.window.createTerminal({
      name: `JugaadLang: ${fileName}`,
      iconPath: new vscode.ThemeIcon('play'),
    });
    terminal.show();
    terminal.sendText(`${jugPath} run "${filePath}"`);
  });
  context.subscriptions.push(runFileCmd);

  // ── Command: Open REPL ──────────────────────────────────────────────────────
  const openReplCmd = vscode.commands.registerCommand('jugaadlang.openRepl', () => {
    const config = vscode.workspace.getConfiguration('jugaadlang');
    const jugPath = config.get<string>('jugPath', 'jug');

    const terminal = vscode.window.createTerminal({
      name: 'JugaadLang REPL',
      iconPath: new vscode.ThemeIcon('terminal'),
    });
    terminal.show();
    terminal.sendText(`${jugPath} repl`);
  });
  context.subscriptions.push(openReplCmd);

  // ── Document Open Listener ──────────────────────────────────────────────────
  context.subscriptions.push(
    vscode.workspace.onDidOpenTextDocument((doc) => {
      if (isJugFile(doc)) {
        maybeShowWelcome(context);
      }
    })
  );

  // Check if a .jug file is already open when extension activates
  if (vscode.window.activeTextEditor && isJugFile(vscode.window.activeTextEditor.document)) {
    maybeShowWelcome(context);
  }
}

// ─────────────────────────────────────────────────────────────────────────────
// Deactivation
// ─────────────────────────────────────────────────────────────────────────────
export function deactivate(): void {
  console.log('JugaadLang extension deactivated. Alvida! 🙏');
}

// ─────────────────────────────────────────────────────────────────────────────
// Helpers
// ─────────────────────────────────────────────────────────────────────────────

function isJugFile(document: vscode.TextDocument): boolean {
  return (
    document.languageId === 'jugaadlang' ||
    document.fileName.endsWith('.jug')
  );
}

function updateStatusBar(editor: vscode.TextEditor | undefined): void {
  if (editor && isJugFile(editor.document)) {
    const fileName = path.basename(editor.document.fileName);
    statusBarItem.text = `🇮🇳 JugaadLang — ${fileName}`;
    statusBarItem.tooltip = `${fileName} — Click to run (Cmd+F5)`;
    statusBarItem.show();
  } else {
    statusBarItem.hide();
  }
}

function maybeShowWelcome(context: vscode.ExtensionContext): void {
  // Use global state so welcome shows only once per install
  const hasShown = context.globalState.get<boolean>('jugaadlang.welcomeShown', false);
  if (hasShown || welcomeShown) {
    return;
  }

  const config = vscode.workspace.getConfiguration('jugaadlang');
  if (!config.get<boolean>('showWelcomeMessage', true)) {
    return;
  }

  welcomeShown = true;
  context.globalState.update('jugaadlang.welcomeShown', true);

  vscode.window
    .showInformationMessage(
      '🇮🇳 JugaadLang mein aapka swagat hai! Desi coding ka asli maza shuru hota hai abhi!',
      'Run File (Cmd+F5)',
      'Open REPL',
      'Nahi chahiye'
    )
    .then((selection) => {
      if (selection === 'Run File (Cmd+F5)') {
        vscode.commands.executeCommand('jugaadlang.runFile');
      } else if (selection === 'Open REPL') {
        vscode.commands.executeCommand('jugaadlang.openRepl');
      }
    });
}
