"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || (function () {
    var ownKeys = function(o) {
        ownKeys = Object.getOwnPropertyNames || function (o) {
            var ar = [];
            for (var k in o) if (Object.prototype.hasOwnProperty.call(o, k)) ar[ar.length] = k;
            return ar;
        };
        return ownKeys(o);
    };
    return function (mod) {
        if (mod && mod.__esModule) return mod;
        var result = {};
        if (mod != null) for (var k = ownKeys(mod), i = 0; i < k.length; i++) if (k[i] !== "default") __createBinding(result, mod, k[i]);
        __setModuleDefault(result, mod);
        return result;
    };
})();
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.activate = activate;
exports.deactivate = deactivate;
const vscode = __importStar(require("vscode"));
const axios_1 = __importDefault(require("axios"));
const path = __importStar(require("path"));
function activate(context) {
    console.log('QA Architect AI activated');
    const disposable = vscode.commands.registerCommand('qa-architect.generateFramework', async () => {
        const prompt = await vscode.window.showInputBox({
            placeHolder: 'Describe the QA framework to generate',
            prompt: 'Example: Generate Selenium Java enterprise framework'
        });
        if (!prompt) {
            return;
        }
        const workspaceFolders = vscode.workspace.workspaceFolders;
        if (!workspaceFolders || workspaceFolders.length === 0) {
            vscode.window.showErrorMessage('Please open a workspace folder first.');
            return;
        }
        const config = vscode.workspace.getConfiguration('qaArchitect');
        const apiUrl = config.get('apiUrl', 'http://127.0.0.1:8001');
        const outputDirSetting = config.get('outputDir', 'generated/test-framework');
        const workspacePath = workspaceFolders[0].uri.fsPath;
        const outputDir = path.isAbsolute(outputDirSetting)
            ? outputDirSetting
            : path.join(workspacePath, outputDirSetting);
        try {
            await vscode.window.withProgress({
                location: vscode.ProgressLocation.Notification,
                title: 'Generating QA Framework...',
                cancellable: false
            }, async () => {
                const response = await axios_1.default.post(`${apiUrl}/generate`, {
                    prompt,
                    output_dir: outputDir
                }, {
                    timeout: 120000
                });
                console.log(response.data);
            });
            const openChoice = await vscode.window.showInformationMessage('Framework generated successfully!', 'Open Folder');
            if (openChoice === 'Open Folder') {
                vscode.commands.executeCommand('vscode.openFolder', vscode.Uri.file(outputDir), true);
            }
        }
        catch (error) {
            const message = error?.response?.data?.detail ||
                error?.message ||
                'Unknown error';
            vscode.window.showErrorMessage(`Generation Failed: ${message}`);
            console.error(error);
        }
    });
    context.subscriptions.push(disposable);
}
function deactivate() { }
//# sourceMappingURL=extension.js.map