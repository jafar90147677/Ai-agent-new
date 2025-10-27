# 🤖 AI Agent - VS Code Extension

AI Agent is a powerful VS Code extension that brings ChatGPT-like AI assistance directly to your workflow. Powered by Ollama and featuring streaming responses, it provides a conversational AI experience similar to ChatGPT for any task you need help with.

## ✨ Features

### 🎯 Core AI Capabilities (ChatGPT-like)
- **Ask AI Agent**: Get intelligent answers to any questions with streaming responses (like ChatGPT)
- **Text Explanation**: Understand complex text with detailed AI explanations
- **Content Analysis**: Analyze and summarize document content
- **Text Improvement**: Get suggestions to improve your writing and content
- **Conversational Interface**: Persistent chat panel for ongoing conversations

### 🚀 Professional UI/UX (ChatGPT-like)
- **Dedicated Activity Bar**: Own sidebar panel with chat and tools
- **ChatGPT-style Interface**: Conversational chat panel with message bubbles
- **Live Events & Quick Actions**: Real-time monitoring with quick access to common tasks
  - **OPEN EDITORS**: Track currently open files
  - **AI AGENT**: Monitor AI status and model information
  - **OUTLINE**: View code structure and symbols
  - **TIMELINE**: Live event feed showing file operations, AI interactions, and system events
  - **QUICK ACTIONS**: One-click access to AI commands, file operations, and VS Code features
- **Status Bar Integration**: Real-time status updates and quick access
- **Context Menus**: Right-click integration for seamless workflow
- **Keyboard Shortcuts**: Fast access with customizable keybindings
- **Streaming Responses**: Real-time AI responses like ChatGPT
- **Persistent Conversations**: Always-available chat interface for ongoing discussions

### ⚙️ Flexible Configuration
- **Multiple AI Models**: Support for Llama3, CodeLlama, Mistral, and Phi3
- **Easy Model Switching**: Dropdown interface for quick model selection with visual feedback
- **Custom Ollama Server**: Configure your own Ollama instance
- **Response Customization**: Choose output format and token limits
- **Status Bar Control**: Show/hide status indicators

## 🛠️ Requirements

- **Ollama**: Install and run Ollama locally
  ```bash
  # Install Ollama (visit https://ollama.ai for instructions)
  ollama pull llama3
  ollama pull codellama
  ```

## 📋 Extension Settings

This extension contributes the following settings:

- `ai-agent.ollamaUrl`: Ollama server URL (default: `http://localhost:11434`)
- `ai-agent.defaultModel`: Default AI model to use (default: `llama3`)
- `ai-agent.enableStreaming`: Enable streaming responses (default: `true`)
- `ai-agent.showStatusBar`: Show AI Agent status in status bar (default: `true`)
- `ai-agent.autoSaveResponses`: Automatically save AI responses (default: `false`)
- `ai-agent.responseLanguage`: Language mode for responses (default: `markdown`)
- `ai-agent.maxTokens`: Maximum tokens for responses (default: `2048`)

## 🎮 Usage

### Activity Bar Panel
Click the 🤖 robot icon in the left activity bar to access:
- **Chat Panel**: Persistent AI chat interface
- **AI Tools**: Quick access to all AI commands

### Keyboard Shortcuts
- `Ctrl+Shift+A` (Cmd+Shift+A on Mac): Ask AI Agent
- `Ctrl+Shift+E` (Cmd+Shift+E on Mac): Explain selected text
- `Ctrl+Shift+T` (Cmd+Shift+T on Mac): Analyze content
- `Ctrl+Shift+C` (Cmd+Shift+C on Mac): Open chat panel
- `Ctrl+Shift+Alt+A` (Cmd+Shift+Alt+A on Mac): Focus AI Agent sidebar

### Context Menu
Right-click in the editor to access:
- Ask AI Agent
- Explain Text (when text is selected)
- Improve Text (when text is selected)
- Analyze Content

### ChatGPT-like Chat Panel
- Type messages and press Enter to chat with AI (just like ChatGPT)
- Real-time streaming responses as you type
- Persistent conversation history within session
- Message bubbles for user and AI responses
- Clear chat history with the Clear button
- All commands automatically open the chat panel for seamless experience

### Command Palette
Access all commands via `Ctrl+Shift+P`:
- `AI Agent: Ask AI Agent`
- `AI Agent: Explain Selected Text`
- `AI Agent: Analyze Content`
- `AI Agent: Improve Text`
- `AI Agent: Show AI Agent Status`
- `AI Agent: Open AI Agent Settings`

## 🔧 Setup

1. **Install Ollama**: Download and install from [ollama.ai](https://ollama.ai)
2. **Pull Models**: Run `ollama pull llama3` and `ollama pull codellama`
3. **Start Ollama**: Ensure Ollama is running on `localhost:11434`
4. **Install Extension**: Install AI Agent from VS Code marketplace
5. **Configure**: Adjust settings in VS Code preferences if needed

## 🐛 Known Issues

- Requires Ollama to be running locally
- Large responses may take time to stream completely
- Some models may require additional memory

## 📝 Release Notes

### 0.0.1

Initial release featuring:
- AI-powered code assistance with streaming responses
- Multiple command support (Ask, Explain, Generate Tests, Optimize)
- Professional UI with status bar integration
- Configurable Ollama integration
- Context menu and keyboard shortcut support

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by professional AI coding tools like Augment AI
- Built with VS Code Extension API
- Powered by Ollama for local AI inference

---

**Enjoy coding with AI assistance!** 🚀
