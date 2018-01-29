### Windows 10 and HIPAA PC Security & Compliance Auditor

##### Windows 10 Settings

CIOs, IT Directors and IT Managers are often deputized as their organization’s HIPAA Security Officer.  In addition to being responsible for HIPAA security and compliance, there may be a push to upgrade to Windows 10.   After all, everyone in the organization is already using it at home.  But during testing and planning deployment, Cortana and the mobile-OS-like features of sending data to third-parties begs the question, “Does Windows 10 violate HIPAA Privacy?”

The short answer is that the default configuration of Windows 10 may violate HIPAA.  The Windows 10 Privacy Statement as part of the Microsoft License terms July 2015 provides very flexible language on how Personal Data is collected, used and shared.    Specifically this provision states:

“We will access, disclose and preserve personal data, including your content (such as the content of your emails, other private communications or files in private folders), when we have a good faith belief that doing so is necessary to protect our customers or enforce the terms governing the use of the services.”

As with any convenient features, there is always an impact on security.  Unfortunately, security and functionality are often inversely related.

Windows 10 Privacy Settings

The following Windows 10 features are new and cause concern for anyone responsible for maintaining HIPAA compliance in their organization:

Cortana: Microsoft’s answer to Siri and Google Talk.  Cortana “learns” how each person speaks and writes by taking samples.  In addition, names, nicknames, recent calendar events and contacts are maintained.

- Data Sync: Default setting allows the operating system to sync settings and data into Microsoft’s servers. It is intended to sync passwords, website plugins, favorites, etc.; however it may lead to users’ credentials being vicariously breached by Microsoft.

- 3rd party Advertisers: The Advertising ID provides a unique identifier per user allowing collections of data to be shared with 3rd party advertisers.  This may help fund the “free” upgrade to Windows 10 from previous versions, and is provided to help provide more effective targeted ads when using 3rd party applications.  Turning this off will not block ads from appearing, but they may not be as targeted, as your users will remain more anonymous with this feature turned off.
- Bitlocker: Windows 10 will automatically backup your encryption key to OneDrive, unless you are using Active Directory Group Policy to manage this element.  Also, if you are using Bitlocker or planning to use Bitlocker, ensure you use the TPM+PIN option or turn off hibernation/sleep support to avoid having to report a breach if a Bitlocker-encrypted laptop is lost or stolen.
- Telemetry:  Those familiar with the Windows Pop-up sending diagnostic information after a program crashes to Microsoft for product improvement will want to know about Telemetry.  Telemetry is an enhanced diagnostics and tracking service which sends additional information to Microsoft for new features such as per-application updates, Windows 10 upgrade offers, etc.  This is a well-documented How-To disable Telemetry from our friends at Winaero.

Although it is still early to tell if specific HIPAA Privacy considerations are violated with Windows 10; HIPAA Privacy, at a high level, ensures individuals have the minimum protections which may be violated. Therefore depending on whether ePHI is released as these Windows 10 features are used; we believe the violation of the following laws may lead to HIPAA non-compliance:

- Access to the health record – see patient rights §164.522, §164.524 §164.526
- Minimum necessary uses of PHI – see use and disclosure §164.514
- Content and right to an Accounting of Disclosures – see privacy management process §164.528
- Business Associate Contracts – see privacy management process §164.504, §164.502, §164.524, §164.526,§164.528.
- To ensure diligence with HIPAA Privacy, it is unclear whether Microsoft will be sending ePHI from PCs anytime soon, which may result in “collateral damage” for those Covered Entities using Windows 10.   And although the question on HIPAA Privacy violations is a tenuous answer, following some basic steps may significantly reduce your organization’s risk of violating HIPAA.

Windows 10 Cortana settings

To maintain your organization’s level of due-diligence under HIPAA and the HITECH act, there are items to configure in Windows 10 to help avoid long-term repercussions that result from upgrading to Windows 10.   By taking measures to test, configure and restrict information being sent outside your organization’s networks with Windows 10; you may request set of instructions below.