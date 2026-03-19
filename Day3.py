#第三天：VR设备帧率分级检测
device_name = input("请输入你的VR设备名称：")
fps = float(input("请输入当前VR设备的运行帧率（FPS）:"))
#多条件区间判断：VR帧率体验分级（临界值：60/90/120FPS）
if fps < 60:
    level = "极差"
    suggestion = "帧率过低，易产生眩晕，建议关闭后台程序/降低画质"
elif 60 <= fps < 90:
    level = "一般"
    suggestion = "基本满足使用，追求流畅体验建议提升硬件配置"
elif 90 <= fps < 120:
    level = "优秀"
    suggestion = "帧率流畅，符合VR沉浸式体验标准"
else:
    level = "极致"
    suggestion = "帧率拉满，适配高端VR设备，体验最佳"
    #统一输出检测结果
    print(f"【{device_name}帧率检测报告】")
    print(f"当前帧率：{fps:.1f}FPS|体验等级：{level}")
    print(f"优化建议:{suggestion}")
